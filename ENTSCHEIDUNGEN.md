# Entscheidungen

Was hier steht, gilt für alle. Grundlage: Lastenheft v1.0 (12.11.2026) und Drehbuch zur Bilderstellung (18.11.2026). Neue Einträge nur nach Bestätigung durch ein Teammitglied, mit Datum und Namen.

## Klassen (Hauptmodell)

| Ordnername | Klasse | Pfand |
| --- | --- | --- |
| `dose` | Dose | 0,25 € |
| `einweg_plastik` | Einweg-Plastikflasche | 0,25 € |
| `bierflasche` | Bierflasche (Glas, braun) | 0,08 € |
| `mehrweg` | Mehrweg-Flasche (Glas) | 0,15 € |
| `kein_pfand` | Kein Pfand | 0,00 € |
| `nichts` | Nichts | – |

Optional Logo-Modell: `dpg_logo`, `mehrweg_logo`, `kein_logo`.

Abgrenzungen: Saft und Milch in PET → `einweg_plastik`. Mehrweg-PET wird nicht aufgenommen. Grüne Bierflaschen sind nicht im Datensatz. Bügelflaschen → `mehrweg`.

## Bilddaten

- Aufnahme mit `aufnahme.py` (OpenCV) über die Laptop-Webcams, 640 × 480 Pixel, JPG.
- 160 Originale pro Klasse: Serien S1–S8 (136 Bilder) + Testsitzung T (24 Bilder).
- Objekte O01–O10 für S1–S8, O11 und O12 nur in der Testsitzung. Bei `nichts` Umgebungen U01–U12.
- Aufteilung 70 / 15 / 15 = 112 / 24 / 24 pro Klasse, **vor** der Augmentation.
- Augmentation nur auf `train/`: Hauptmodell ×3, Logo-Modell ×2. Kein Farbton-Wechsel, keine Graustufen, kein vertikales Spiegeln.
- Dateiname: `<klasse>_<serie>_<objekt>_<kürzel>_<nr>.jpg`, z. B. `dose_S03_O05_ER_0012.jpg`. Varianten: `..._aug2.jpg`.
- Personenkürzel: ER, KL, SS, MH.
- Protokoll: `daten/aufnahmeprotokoll.csv` mit Spalten `dateiname,klasse,serie,objekt,hintergrund,licht,perspektive,abstand,ausrichtung,haltung,person,datum,split`.

## Speicherort der Bilder (bestätigt von Erika Rohrmeyer, 19.11.2026)

- Gemeinsamer Cloud-Ordner: OneDrive-Ordner `ki-pfandautomat-bilder`. Besitzerin ist Erika Rohrmeyer, freigegeben für Katharina Lutzky, Sita Stojan und Manuel Herrmann.
- Jede Person synchronisiert den Ordner lokal und gibt ihn bei der Aufnahme mit `--datenordner` an. Der lokale Pfad ist an jedem Laptop anders. Beim Schulkonto heißt der OneDrive-Ordner „OneDrive - Rudolf-Diesel-Fachschule - Nürnberg“, z. B. bei Erika:
  `python skripte/aufnahme.py --klasse mehrweg --serie S1 --person ER --datenordner "C:\Users\erika\OneDrive - Rudolf-Diesel-Fachschule - Nürnberg\ki-pfandautomat-bilder"`
  Eigenen Pfad finden: im Explorer Rechtsklick auf den Ordner → „Als Pfad kopieren“. Anführungszeichen nicht vergessen (Leerzeichen im Pfad).

## Technik (aus dem Lastenheft)

Python 3, TensorFlow (Transfer Learning), OpenCV, NumPy, Pillow, Matplotlib, Tkinter, VSCode, GitHub. Schwellenwert für sichere Erkennung: 80 %.
