# KI-Log

Neueste Einträge oben. Format siehe `KI-REGELN.md`.

## 2026-11-19 12:20 · KI-Manuel (für Manuel)
- Was: Lastenheft und überarbeitetes Drehbuch ins Repo gelegt, damit alle KIs darauf zugreifen können. Das Repo ist ab jetzt der einzige Projektordner.
- Dateien: doku/Lastenheft_Pfandautomat.docx, doku/Drehbuch_Pfandautomat.pdf, STATUS.md
- Offen/Hinweis: Neue Projektdokumente bitte ebenfalls in doku/ ablegen.

## 2026-11-19 12:15 · KI-Manuel (für Manuel)
- Was: Aufnahmeskript geschrieben. Live-Bild, Leertaste speichert ein Bild, Dateiname und Protokollzeile automatisch nach ENTSCHEIDUNGEN.md, Aufnahmeplan S1–S8/T und Logo-Serien hinterlegt (Zielanzahl und erlaubte Merkmale je Serie), Schärfe-Warnung, z = letztes Bild löschen. Logo-Klassen speichern nur den markierten Ausschnitt (320 × 320) unter daten/logo/.
- Dateien: skripte/aufnahme.py, requirements.txt, STATUS.md
- Offen/Hinweis: Logik ohne Webcam getestet, auch Pfade mit Umlauten. Test an echter Webcam steht noch aus. Im Protokoll steht bei S1–S8 split = "offen", aufteilung.py setzt später train/val. Start: `python skripte/aufnahme.py --klasse dose --serie S1 --person MH`

## 2026-11-19 12:00 · KI-Manuel (für Manuel)
- Was: Uni Brain eingerichtet: Regeln, Entscheidungen aus Lastenheft und Drehbuch, Status mit Zeitplan
- Dateien: KI-REGELN.md, ENTSCHEIDUNGEN.md, STATUS.md, KI-LOG.md, CLAUDE.md, AGENTS.md, .gitignore
- Offen/Hinweis: Alle KIs lesen zuerst KI-REGELN.md
