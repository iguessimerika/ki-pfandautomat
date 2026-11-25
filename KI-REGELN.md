# KI-Regeln – Uni Brain Pfandautomat

Diese Datei liest jede KI **zuerst**, bevor sie im Repo etwas tut. Teammitglieder geben ihrer KI zu Beginn einfach diesen Satz:

> Lies zuerst `KI-REGELN.md`, `STATUS.md`, `ENTSCHEIDUNGEN.md` und die letzten 20 Einträge in `KI-LOG.md` in unserem Repo https://github.com/iguessimerika/ki-pfandautomat und halte dich an die Regeln.

KIs, die `CLAUDE.md` oder `AGENTS.md` automatisch lesen (z. B. Claude Code, Codex), bekommen diesen Hinweis dort schon von selbst.

## Kennzeichnung

| Teammitglied | Kürzel der KI | Commit-Präfix |
| --- | --- | --- |
| Erika Rohrmeyer | KI-Erika | `[KI-Erika]` |
| Katharina Lutzky | KI-Katha | `[KI-Katha]` |
| Sita Stojan | KI-Sita | `[KI-Sita]` |
| Manuel Herrmann | KI-Manuel | `[KI-Manuel]` |

Änderungen, die ein Mensch selbst macht, bekommen das Präfix ohne „KI-“, z. B. `[Erika]`.

## Regeln

1. **Vor der Arbeit lesen:** `STATUS.md`, `ENTSCHEIDUNGEN.md` und die letzten Einträge in `KI-LOG.md`. Immer zuerst `git pull`.
2. **Arbeit anmelden:** Bevor eine KI eine Datei ändert, trägt sie sich in `STATUS.md` unter „In Arbeit“ ein (Wer, Was, Dateien). Steht dort schon jemand anderes bei derselben Datei, wird diese Datei nicht angefasst, sondern nachgefragt.
3. **Nichts von anderen überschreiben:** Einträge, Code oder Texte einer anderen Person werden nicht gelöscht oder umgeschrieben. Vorschläge dazu kommen als Eintrag in `KI-LOG.md` mit dem Wort **VORSCHLAG** oder als GitHub-Issue.
4. **Entscheidungen einhalten:** Was in `ENTSCHEIDUNGEN.md` steht, gilt. Neue Entscheidungen trifft das Team, nicht die KI. Die KI darf sie nur eintragen, wenn ein Mensch sie bestätigt hat (mit Namen).
5. **Nach der Arbeit protokollieren:** Jede Änderung bekommt einen Eintrag **oben** in `KI-LOG.md`, der Status in `STATUS.md` wird aktualisiert und die Anmeldung unter „In Arbeit“ entfernt.
6. **Kleine Commits:** Ein Commit pro Aufgabe, Nachricht mit Präfix, z. B. `[KI-Katha] Objektliste für dose ergänzt`.
7. **Keine Bilder ins Repo:** Die Bilder liegen im gemeinsamen Cloud-Ordner. Bilddateien und die Bildordner unter `daten/` stehen in der `.gitignore`. Ins Repo kommen nur Skripte, CSV-Listen (z. B. `daten/objektliste.csv`) und Dokumente. Die Aufnahmeprotokolle liegen bei den Bildern im Cloud-Ordner (siehe `ENTSCHEIDUNGEN.md`).
8. **Unsicher? Fragen statt raten.** Widerspricht etwas dem Drehbuch oder dem Lastenheft, schreibt die KI einen Eintrag mit **FRAGE** in `KI-LOG.md` und sagt es ihrem Menschen.

## Format für KI-LOG.md

```
## 2026-11-19 12:10 · KI-Katha (für Katharina)
- Was: Objektliste für dose und einweg_plastik angelegt (O01–O12)
- Dateien: daten/objektliste.csv
- Offen/Hinweis: Für mehrweg fehlen noch 3 Objekte
```
