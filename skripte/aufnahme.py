"""
aufnahme.py – Webcam-Aufnahme für den Bilddatensatz Pfandautomat.

Zeigt das Live-Bild der Webcam. Pro Tastendruck wird genau ein Bild gespeichert,
automatisch benannt und im Aufnahmeprotokoll eingetragen (siehe ENTSCHEIDUNGEN.md).

Start (Beispiel, aus dem Repo-Ordner):
    python skripte/aufnahme.py --klasse dose --serie S3 --person MH

Optionen:
    --klasse       dose | einweg_plastik | bierflasche | mehrweg | kein_pfand | nichts
                   (Logo-Modell: dpg_logo | mehrweg_logo | kein_logo)
    --serie        S1 ... S8, T (Hauptmodell) bzw. V, LG1 ... LG4, LT (Logo-Modell)
    --person       ER | KL | SS | MH
    --objekt       Start-Objekt, z. B. O01 (bei "nichts": U01). Standard: erstes erlaubtes
    --kamera       Index der Webcam, Standard 0
    --datenordner  Ordner für Bilder und Protokoll, Standard: daten (im Repo-Ordner).
                   Hier kann auch der gemeinsame Cloud-Ordner angegeben werden.

Tasten im Aufnahmefenster:
    Leertaste  Bild speichern
    n / b      nächstes / vorheriges Objekt (bzw. Umgebung bei "nichts")
    h l p a r g   Hintergrund / Licht / Perspektive / Abstand / Ausrichtung / Haltung
               auf den nächsten für diese Serie erlaubten Wert schalten
    z          letztes Bild dieser Sitzung löschen (Datei und Protokollzeile)
    q / Esc    beenden

Hinweis: Die Aufteilung in train / val / test macht später aufteilung.py.
Im Protokoll steht deshalb bei S1–S8 "offen" und bei T/LT direkt "test".
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import sys
from pathlib import Path

import cv2
import numpy as np

# --------------------------------------------------------------------------
# Festlegungen aus Drehbuch und ENTSCHEIDUNGEN.md
# --------------------------------------------------------------------------

KLASSEN_HAUPT = ["dose", "einweg_plastik", "bierflasche", "mehrweg", "kein_pfand", "nichts"]
KLASSEN_LOGO = ["dpg_logo", "mehrweg_logo", "kein_logo"]
PERSONEN = {"ER": "Erika Rohrmeyer", "KL": "Katharina Lutzky", "SS": "Sita Stojan", "MH": "Manuel Herrmann"}

ALLE_WERTE = {
    "hintergrund": ["H1", "H2", "H3", "H4"],
    "licht": ["L1", "L2", "L3", "L4"],
    "perspektive": ["P1", "P2", "P3", "P4"],
    "abstand": ["A1", "A2", "A3"],
    "ausrichtung": ["R1", "R2", "R3", "R4"],
    "haltung": ["G1", "G2", "G3"],
}
MERKMAL_TASTEN = {"h": "hintergrund", "l": "licht", "p": "perspektive",
                  "a": "abstand", "r": "ausrichtung", "g": "haltung"}

# Aufnahmeplan pro Klasse (Drehbuch, Abschnitt 2.3). Fehlende Merkmale = alle Werte erlaubt.
PLAN_HAUPT = {
    "S1": {"ziel": 20, "hintergrund": ["H1"], "licht": ["L1"], "perspektive": ["P1"], "abstand": ["A2"],
           "ausrichtung": ["R1"], "haltung": ["G1"]},
    "S2": {"ziel": 18, "hintergrund": ["H1"], "licht": ["L2"], "perspektive": ["P1", "P4"], "abstand": ["A1"],
           "ausrichtung": ["R1", "R2"], "haltung": ["G1"]},
    "S3": {"ziel": 18, "hintergrund": ["H2"], "licht": ["L2"], "perspektive": ["P1", "P2"], "abstand": ["A2"],
           "ausrichtung": ["R1", "R2"], "haltung": ["G1"]},
    "S4": {"ziel": 16, "hintergrund": ["H2"], "licht": ["L1"], "perspektive": ["P1", "P3"], "abstand": ["A3"],
           "ausrichtung": ["R1"], "haltung": ["G1", "G3"]},
    "S5": {"ziel": 16, "hintergrund": ["H1", "H2"], "licht": ["L3"], "perspektive": ["P1", "P3"], "abstand": ["A2"],
           "ausrichtung": ["R1", "R2"], "haltung": ["G1"]},
    "S6": {"ziel": 16, "hintergrund": ["H4"], "licht": ["L4"], "perspektive": ["P2", "P4"], "abstand": ["A1", "A2"],
           "ausrichtung": ["R2", "R3"], "haltung": ["G1"]},
    "S7": {"ziel": 16, "hintergrund": ["H3"], "licht": ["L2"], "perspektive": ["P1", "P2"], "abstand": ["A2"],
           "ausrichtung": ["R1", "R3", "R4"], "haltung": ["G1"]},
    "S8": {"ziel": 16, "ausrichtung": ["R3", "R4"], "haltung": ["G2", "G3"]},
    "T": {"ziel": 24},
}
# Logo-Modell (Drehbuch, Abschnitt 2.4)
PLAN_LOGO = {
    "V": {"ziel": 30, "licht": ["L1", "L2"]},
    "LG1": {"ziel": 60, "licht": ["L1", "L2"]},
    "LG2": {"ziel": 50, "licht": ["L1", "L2"]},
    "LG3": {"ziel": 40, "licht": ["L3", "L4"]},
    "LG4": {"ziel": 20},
    "LT": {"ziel": 30},
}

PROTOKOLL_SPALTEN = ["dateiname", "klasse", "serie", "objekt", "hintergrund", "licht", "perspektive",
                     "abstand", "ausrichtung", "haltung", "person", "datum", "split"]

BILD_BREITE, BILD_HOEHE = 640, 480
LOGO_AUSSCHNITT = 320          # Kantenlänge des markierten Ausschnitts in der Bildmitte (Logo-Modell)
SCHAERFE_GRENZE = 70.0         # darunter Warnung "unscharf" (Probelauf 19.11.: scharf 77–128, verwackelt 59–64)


# --------------------------------------------------------------------------
# Hilfsfunktionen (ohne Kamera, daher testbar)
# --------------------------------------------------------------------------

def ist_logo(klasse: str) -> bool:
    return klasse in KLASSEN_LOGO


def plan_fuer(klasse: str, serie: str) -> dict:
    plan = PLAN_LOGO if ist_logo(klasse) else PLAN_HAUPT
    if serie not in plan:
        raise ValueError(f"Serie {serie} gibt es für diese Klasse nicht. Erlaubt: {', '.join(plan)}")
    eintrag = plan[serie]
    return {m: eintrag.get(m, werte) for m, werte in ALLE_WERTE.items()} | {"ziel": eintrag["ziel"]}


def erlaubte_objekte(klasse: str, serie: str) -> list[str]:
    """O01–O10 für S1–S8, O11/O12 zusätzlich in der Testsitzung. Bei 'nichts' Umgebungen U01–U12."""
    buchstabe = "U" if klasse == "nichts" else "O"
    nummern = range(1, 11) if re.fullmatch(r"S\d", serie) else range(1, 13)
    return [f"{buchstabe}{n:02d}" for n in nummern]


def serie_im_dateinamen(serie: str) -> str:
    """S3 -> S03, LG1 -> LG01, T bleibt T (wie im Drehbuch: dose_S03_..., nichts_T_...)."""
    treffer = re.fullmatch(r"([A-Z]+)(\d+)", serie)
    return f"{treffer.group(1)}{int(treffer.group(2)):02d}" if treffer else serie


def split_fuer(serie: str) -> str:
    return "test" if serie in ("T", "LT") else ("vortest" if serie == "V" else "offen")


def ordner_fuer(datenordner: Path, klasse: str) -> tuple[Path, Path]:
    """Gibt (Bildordner, Protokolldatei) zurück."""
    basis = datenordner / "logo" if ist_logo(klasse) else datenordner
    return basis / "originale" / klasse, basis / "aufnahmeprotokoll.csv"


def naechste_nummer(bildordner: Path, praefix: str) -> int:
    hoechste = 0
    if bildordner.exists():
        for datei in bildordner.glob(f"{praefix}_*.jpg"):
            treffer = re.fullmatch(re.escape(praefix) + r"_(\d{4})\.jpg", datei.name)
            if treffer:
                hoechste = max(hoechste, int(treffer.group(1)))
    return hoechste + 1


def bild_schreiben(pfad: Path, bild: np.ndarray) -> None:
    """cv2.imwrite scheitert unter Windows an Umlauten im Pfad (z. B. 'Fächer'), daher über imencode."""
    ok, puffer = cv2.imencode(".jpg", bild, [cv2.IMWRITE_JPEG_QUALITY, 95])
    if not ok:
        raise OSError("Bild konnte nicht kodiert werden")
    pfad.write_bytes(puffer.tobytes())


def protokoll_anhaengen(protokoll: Path, zeile: dict) -> None:
    neu = not protokoll.exists()
    protokoll.parent.mkdir(parents=True, exist_ok=True)
    with protokoll.open("a", newline="", encoding="utf-8") as f:
        schreiber = csv.DictWriter(f, fieldnames=PROTOKOLL_SPALTEN)
        if neu:
            schreiber.writeheader()
        schreiber.writerow(zeile)


def protokoll_zeile_entfernen(protokoll: Path, dateiname: str) -> None:
    with protokoll.open(newline="", encoding="utf-8") as f:
        zeilen = list(csv.DictReader(f))
    with protokoll.open("w", newline="", encoding="utf-8") as f:
        schreiber = csv.DictWriter(f, fieldnames=PROTOKOLL_SPALTEN)
        schreiber.writeheader()
        schreiber.writerows(z for z in zeilen if z["dateiname"] != dateiname)


def zaehlen(protokoll: Path, klasse: str, serie: str) -> tuple[int, dict[str, int]]:
    """Anzahl Bilder dieser Klasse und Serie (alle Personen) und Anzahl je Objekt."""
    gesamt, je_objekt = 0, {}
    if protokoll.exists():
        with protokoll.open(newline="", encoding="utf-8") as f:
            for z in csv.DictReader(f):
                if z["klasse"] == klasse and z["serie"] == serie:
                    gesamt += 1
                    je_objekt[z["objekt"]] = je_objekt.get(z["objekt"], 0) + 1
    return gesamt, je_objekt


def schaerfe(bild: np.ndarray) -> float:
    return float(cv2.Laplacian(cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var())


def logo_ausschnitt(bild: np.ndarray) -> tuple[int, int, int, int]:
    h, w = bild.shape[:2]
    k = min(LOGO_AUSSCHNITT, h, w)
    x, y = (w - k) // 2, (h - k) // 2
    return x, y, k, k


def speichern(bild: np.ndarray, datenordner: Path, klasse: str, serie: str, objekt: str,
              person: str, merkmale: dict[str, str]) -> Path:
    """Speichert ein Bild mit Dateinamen nach Schema und schreibt die Protokollzeile."""
    bildordner, protokoll = ordner_fuer(datenordner, klasse)
    bildordner.mkdir(parents=True, exist_ok=True)
    praefix = f"{klasse}_{serie_im_dateinamen(serie)}_{objekt}_{person}"
    pfad = bildordner / f"{praefix}_{naechste_nummer(bildordner, praefix):04d}.jpg"
    if ist_logo(klasse):
        x, y, b, h = logo_ausschnitt(bild)
        bild = bild[y:y + h, x:x + b]
    bild_schreiben(pfad, bild)
    protokoll_anhaengen(protokoll, {
        "dateiname": pfad.name, "klasse": klasse, "serie": serie, "objekt": objekt, **merkmale,
        "person": person, "datum": dt.date.today().isoformat(), "split": split_fuer(serie),
    })
    return pfad


# --------------------------------------------------------------------------
# Aufnahme mit Webcam
# --------------------------------------------------------------------------

def text(bild, zeile: int, inhalt: str, farbe=(255, 255, 255)) -> None:
    y = 22 + zeile * 22
    cv2.putText(bild, inhalt, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(bild, inhalt, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.55, farbe, 1, cv2.LINE_AA)


def kamera_oeffnen(index: int) -> cv2.VideoCapture:
    kamera = cv2.VideoCapture(index, cv2.CAP_DSHOW) if os.name == "nt" else cv2.VideoCapture(index)
    kamera.set(cv2.CAP_PROP_FRAME_WIDTH, BILD_BREITE)
    kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, BILD_HOEHE)
    if not kamera.isOpened():
        sys.exit(f"Webcam {index} lässt sich nicht öffnen. Anderen Index mit --kamera probieren.")
    return kamera


def aufnehmen(args: argparse.Namespace) -> None:
    plan = plan_fuer(args.klasse, args.serie)
    objekte = erlaubte_objekte(args.klasse, args.serie)
    if args.objekt and args.objekt not in objekte:
        sys.exit(f"Objekt {args.objekt} ist in Serie {args.serie} nicht erlaubt. Erlaubt: {objekte[0]}–{objekte[-1]}")
    objekt_nr = objekte.index(args.objekt) if args.objekt else 0
    merkmale = {m: plan[m][0] for m in ALLE_WERTE}
    _, protokoll = ordner_fuer(args.datenordner, args.klasse)
    sitzung: list[Path] = []
    meldung, meldung_farbe = "", (255, 255, 255)

    kamera = kamera_oeffnen(args.kamera)
    fenster = "Aufnahme Pfandautomat"
    cv2.namedWindow(fenster)
    print(__doc__.split("Tasten im Aufnahmefenster:")[1].split("Hinweis:")[0])

    while True:
        ok, bild = kamera.read()
        if not ok:
            meldung, meldung_farbe = "Kein Kamerabild!", (0, 0, 255)
            if cv2.waitKey(100) & 0xFF in (ord("q"), 27):
                break
            continue
        if bild.shape[1] != BILD_BREITE or bild.shape[0] != BILD_HOEHE:
            bild = cv2.resize(bild, (BILD_BREITE, BILD_HOEHE))

        objekt = objekte[objekt_nr]
        gesamt, je_objekt = zaehlen(protokoll, args.klasse, args.serie)
        scharf = schaerfe(bild)
        anzeige = bild.copy()
        if ist_logo(args.klasse):
            x, y, b, h = logo_ausschnitt(anzeige)
            cv2.rectangle(anzeige, (x, y), (x + b, y + h), (0, 255, 255), 2)
        text(anzeige, 0, f"{args.klasse} | Serie {args.serie} | {objekt} | {PERSONEN[args.person]}")
        text(anzeige, 1, f"Serie: {gesamt}/{plan['ziel']} Bilder | {objekt}: {je_objekt.get(objekt, 0)}",
             (0, 255, 0) if gesamt >= plan["ziel"] else (255, 255, 255))
        text(anzeige, 2, "  ".join(merkmale.values()))
        text(anzeige, 3, f"Schaerfe {scharf:.0f}" + ("  UNSCHARF" if scharf < SCHAERFE_GRENZE else ""),
             (0, 0, 255) if scharf < SCHAERFE_GRENZE else (255, 255, 255))
        if meldung:
            text(anzeige, 4, meldung, meldung_farbe)
        cv2.imshow(fenster, anzeige)

        taste = cv2.waitKey(1) & 0xFF
        if taste in (ord("q"), 27) or cv2.getWindowProperty(fenster, cv2.WND_PROP_VISIBLE) < 1:
            break
        if taste == ord(" "):
            pfad = speichern(bild, args.datenordner, args.klasse, args.serie, objekt, args.person, merkmale)
            sitzung.append(pfad)
            meldung, meldung_farbe = f"Gespeichert: {pfad.name}", (0, 255, 0)
            if scharf < SCHAERFE_GRENZE:
                meldung, meldung_farbe = "Gespeichert, aber unscharf: mit z loeschen?", (0, 165, 255)
        elif taste == ord("n"):
            objekt_nr = (objekt_nr + 1) % len(objekte)
        elif taste == ord("b"):
            objekt_nr = (objekt_nr - 1) % len(objekte)
        elif chr(taste) in MERKMAL_TASTEN:
            m = MERKMAL_TASTEN[chr(taste)]
            werte = plan[m]
            merkmale[m] = werte[(werte.index(merkmale[m]) + 1) % len(werte)]
        elif taste == ord("z"):
            if sitzung:
                letzte = sitzung.pop()
                letzte.unlink(missing_ok=True)
                protokoll_zeile_entfernen(protokoll, letzte.name)
                meldung, meldung_farbe = f"Geloescht: {letzte.name}", (0, 165, 255)
            else:
                meldung, meldung_farbe = "In dieser Sitzung noch kein Bild gespeichert", (0, 165, 255)

    kamera.release()
    cv2.destroyAllWindows()
    print(f"{len(sitzung)} Bilder in dieser Sitzung gespeichert.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Webcam-Aufnahme für den Datensatz Pfandautomat")
    parser.add_argument("--klasse", required=True, choices=KLASSEN_HAUPT + KLASSEN_LOGO)
    parser.add_argument("--serie", required=True, type=str.upper)
    parser.add_argument("--person", required=True, type=str.upper, choices=list(PERSONEN))
    parser.add_argument("--objekt", type=str.upper)
    parser.add_argument("--kamera", type=int, default=0)
    parser.add_argument("--datenordner", type=Path,
                        default=Path(__file__).resolve().parent.parent / "daten")
    args = parser.parse_args()
    try:
        plan_fuer(args.klasse, args.serie)
    except ValueError as fehler:
        parser.error(str(fehler))
    aufnehmen(args)


if __name__ == "__main__":
    main()
