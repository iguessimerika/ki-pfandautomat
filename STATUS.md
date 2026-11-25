# Status

Zuletzt aktualisiert: 2026-11-25

## In Arbeit (hier anmelden, bevor du Dateien änderst)

| Wer | Was | Dateien | Seit |
| --- | --- | --- | --- |
| | | | |

## Aufträge an die KIs (Stand 19.11.2026)

Jede KI arbeitet die Aufträge mit ihrem Kürzel ab, meldet sich vorher unter „In Arbeit“ an und hakt danach ab. Grundlage ist der Zeitplan im Drehbuch (`dokumente/Drehbuch_Pfandautomat_v1.0.pdf`).

**KI-Katha (für Katharina), bis 20.11.2026**

- [x] `daten/objektliste.csv` anlegen, Spalten `objekt,klasse,beschreibung,nur_test`. Pro Klasse O01–O12, dabei O11 und O12 mit `nur_test = ja`. Für `nichts` Umgebungen U01–U12. Beschreibung kurz, z. B. „Energy-Drink-Dose 0,25 l, blau-silber“. Die Gegenstände nennt Katharina.
- [ ] Katharina eine Liste geben, welche Gegenstände pro Klasse noch fehlen (Ziel: 12 je Klasse).
- [ ] Probelauf an Katharinas Laptop begleiten: `python skripte/aufnahme.py --klasse dose --serie S1 --person KL`, ca. 5 Bilder pro Klasse. Schärfewerte und Probleme als Eintrag ins KI-LOG, Probebilder danach löschen.

**KI-Erika (für Erika), bis 20.11.2026**

- [x] Mit Erika den gemeinsamen Cloud-Ordner für die Bilder festlegen. Den Pfad nach Erikas Bestätigung in `ENTSCHEIDUNGEN.md` eintragen. Er wird beim Aufnehmen mit `--datenordner` angegeben.
- [x] Erika daran erinnern, Katharina, Sita und Manuel im Repo als Collaborators einzuladen (GitHub → Settings → Collaborators).
- [ ] Probelauf an Erikas Laptop begleiten: `python skripte/aufnahme.py --klasse mehrweg --serie S1 --person ER`, ca. 5 Bilder pro Klasse. Ergebnis ins KI-LOG, Probebilder danach löschen.
- [ ] Danach (bis 01.12.2026): `skripte/aufteilung.py` planen, siehe Drehbuch Abschnitt 5 (Validierung nicht zufällig, sondern pro Serie die Bilder eines Objekts, das in dieser Serie nicht im Training liegt).

**KI-Manuel (für Manuel), bis 20.11.2026**

- [x] Probelauf an Manuels Laptop, Schärfegrenze in `aufnahme.py` anpassen (19.11., Grenze jetzt 70)
- [ ] Logo-Vortest (20–30 Fotos, Serie V)

## Offen (laut Zeitplan im Drehbuch)

| Aufgabe | Verantwortlich | Bis |
| --- | --- | --- |
| Gegenstände sammeln, `objektliste.csv` anlegen | Katharina Lutzky | 20.11.2026 |
| Repo, Cloud-Ordner und Ordnerstruktur einrichten | Erika Rohrmeyer | 19.11.2026 |
| `aufnahme.py` an den Laptop-Webcams testen (Skript ist geschrieben) | Manuel Herrmann, Erika Rohrmeyer | 20.11.2026 |
| Logo-Vortest (20–30 Testfotos) | Manuel Herrmann | 20.11.2026 |
| Probelauf: ca. 5 Bilder pro Klasse an jedem Laptop, danach löschen | alle | 20.11.2026 |
| Trainingssitzung S1–S6 zu Hause, S7/S8 im Unterricht | Katharina Lutzky, Erika Rohrmeyer, Manuel Herrmann | 27.11.2026 |
| Testsitzung T | ~~Sita Stojan~~ fällt auf unbestimmte Zeit aus, **Ersatz offen (Team entscheidet)** | 30.11.2026 |
| Aufteilung, Prüfung, Augmentation, Zählung | Erika Rohrmeyer, Katharina Lutzky | 01.12.2026 |

## Erledigt

| Datum | Was | Wer |
| --- | --- | --- |
| 25.11.2026 | `dose`: 9 von 12 Dosen vorhanden (O01–O08, O11), O09, O10, O12 fehlen noch | Katharina, KI-Katha |
| 25.11.2026 | Ein Protokoll pro Person (`aufnahmeprotokoll_<Kürzel>.csv`), `aufnahme.py` angepasst | KI-Manuel |
| 19.11.2026 | `einweg_plastik` S7: 12 von 16 Bildern (O01–O06), seit 25.11. im Cloud-Ordner | Manuel |
| 18.11.2026 | Drehbuch zur Bilderstellung überarbeitet | Team |
| 19.11.2026 | Uni-Brain-Dateien angelegt | KI-Manuel |
| 19.11.2026 | `skripte/aufnahme.py` geschrieben (ohne Webcam getestet) | KI-Manuel |
| 19.11.2026 | Lastenheft v1.0 und Drehbuch v1.0 als PDF unter `dokumente/` abgelegt | KI-Katha |
| 19.11.2026 | `daten/objektliste.csv` als Gerüst angelegt (72 Zeilen, Beschreibungen noch leer) | KI-Katha |
| 19.11.2026 | `daten/objektliste.csv` mit geplanten Gegenständen gefüllt (gängige Produkte in Deutschland, noch nicht gesammelt) | KI-Katha |
| 19.11.2026 | Katharina, Sita und Manuel als Collaborators im Repo eingeladen | Erika |
| 19.11.2026 | Cloud-Ordner `ki-pfandautomat-bilder` (OneDrive) angelegt, freigegeben und in `ENTSCHEIDUNGEN.md` eingetragen | Erika, KI-Erika |
