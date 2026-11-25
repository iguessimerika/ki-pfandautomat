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
- Gegenstände pro Aufnahmetag (ab 25.11.2026, Abweichung vom Drehbuch): Keine feste Liste mehr, weil in der Schule immer andere Flaschen und Dosen da sind. Wer aufnimmt, nummeriert die Gegenstände, die er an diesem Tag vor sich hat: F01, F02 … (bei `nichts` Umgebungen U01, U02 …), egal welche Marke. Eindeutig ist ein Gegenstand über Datum + Person + Nummer (stehen im Protokoll). Innerhalb eines Tages bleibt F01 derselbe Gegenstand. Pro Serie möglichst viele verschiedene Gegenstände.
- Validierung: `aufteilung.py` gruppiert nach Datum + Person + Gegenstand und nimmt pro Serie die Bilder ganzer Gegenstände in die Validierung, nie einzelne Bilder.
- Testsitzung: Sita nimmt Gegenstände, die in keinem Trainingsbild vorkommen. Da die Flaschen sowieso wechseln, reicht es, keine bereits fotografierte Flasche zu verwenden.
- Ältere Bilder mit O-Nummern (Manuel, `einweg_plastik` S7 am 19.11. und S8 am 25.11.) bleiben gültig, die O-Nummer gilt dort als Gegenstand dieses Tages. Bei S8 vom 25.11. stimmen die Nummern nicht sicher mit den Flaschen überein, diese 16 Bilder deshalb nur ins Training.
- `daten/objektliste.csv` wird zum Fotografieren nicht mehr gebraucht und bleibt nur als Ideensammlung, welche Gegenstände in eine Klasse passen.
(Bestätigt von Manuel Herrmann, 25.11.2026, auf Wunsch des Teams.)
- Aufteilung 70 / 15 / 15 = 112 / 24 / 24 pro Klasse, **vor** der Augmentation.
- Augmentation nur auf `train/`: Hauptmodell ×3, Logo-Modell ×2. Kein Farbton-Wechsel, keine Graustufen, kein vertikales Spiegeln.
- Dateiname: `<klasse>_<serie>_<objekt>_<kürzel>_<nr>.jpg`, z. B. `dose_S03_F05_ER_0012.jpg`. Varianten: `..._aug2.jpg`.
- Personenkürzel: ER, KL, SS, MH.
- Protokoll: ein eigenes Protokoll pro Person im Datenordner (also im Cloud-Ordner neben `originale/`): `aufnahmeprotokoll_ER.csv`, `aufnahmeprotokoll_KL.csv`, `aufnahmeprotokoll_MH.csv`, `aufnahmeprotokoll_SS.csv`. Jede Datei schreibt nur ein Laptop, dadurch gibt es keine OneDrive-Konflikte. `aufnahme.py` wählt die Datei über `--person` und zählt für die Anzeige alle Protokolle zusammen. `aufteilung.py` führt sie später zusammen. Logo-Modell genauso unter `logo/`. Spalten: `dateiname,klasse,serie,objekt,hintergrund,licht,perspektive,abstand,ausrichtung,haltung,person,datum,split`. (Bestätigt von Manuel Herrmann, 25.11.2026, Antwort auf die FRAGE von KI-Erika vom 19.11.)

## Speicherort der Bilder (bestätigt von Erika Rohrmeyer, 19.11.2026)

- Gemeinsamer Cloud-Ordner: OneDrive-Ordner `ki-pfandautomat-bilder`. Besitzerin ist Erika Rohrmeyer, freigegeben für Katharina Lutzky, Sita Stojan und Manuel Herrmann.
- Jede Person synchronisiert den Ordner lokal und gibt ihn bei der Aufnahme mit `--datenordner` an. Der lokale Pfad ist an jedem Laptop anders. Beim Schulkonto heißt der OneDrive-Ordner „OneDrive - Rudolf-Diesel-Fachschule - Nürnberg“, z. B. bei Erika:
  `python skripte/aufnahme.py --klasse mehrweg --serie S1 --person ER --datenordner "C:\Users\erika\OneDrive - Rudolf-Diesel-Fachschule - Nürnberg\ki-pfandautomat-bilder"`
  Eigenen Pfad finden: im Explorer Rechtsklick auf den Ordner → „Als Pfad kopieren“. Anführungszeichen nicht vergessen (Leerzeichen im Pfad).
  Wer den Ordner über „Verknüpfung zu ‚Meine Dateien‘ hinzufügen“ einbindet, bekommt ihn mit vorangestelltem Besitzernamen, z. B. bei Manuel: `C:\Users\mh450\OneDrive - Rudolf-Diesel-Fachschule - Nürnberg\Rohrmeyer Erika's files - ki-pfandautomat-bilder`.

## Technik (aus dem Lastenheft)

Python 3, TensorFlow (Transfer Learning), OpenCV, NumPy, Pillow, Matplotlib, Tkinter, VSCode, GitHub. Schwellenwert für sichere Erkennung: 80 %.
