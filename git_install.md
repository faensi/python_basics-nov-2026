# Git installieren und den Kursordner holen

Die Kursdateien liegen auf GitHub, und du holst sie mit Git über HTTPS. Die Adresse beginnt mit `https://`. Einen SSH-Schlüssel richtest du dafür nicht ein.

Der Ordner nach dem Klonen heißt `python_basics-nov-2026`. Das ist der Kursordner. Spyder verwendet genau diesen Ordner als Arbeitsverzeichnis.

## Git für Windows installieren

1. Öffne [https://git-scm.com/download/win](https://git-scm.com/download/win) und lade den Installer herunter.
2. Starte den Installer. Die vorgeschlagenen Optionen passen. Lass **Git Credential Manager** ausgewählt.
3. Schließe ein schon offenes Terminal und öffne ein neues Fenster, zum Beispiel PowerShell oder die Miniforge Prompt. Erst das neue Fenster kennt den Befehl `git`.
4. Prüfe die Installation:

```bash
git --version
```

Es erscheint eine Zeile, die mit `git version` beginnt.

Auf einem anderen System installierst du Git mit der Paketverwaltung dieses Systems. Die Befehle `git clone` und `git pull` unten bleiben dieselben.

## Kursordner zum ersten Mal holen

Wechsle in den Ordner, in dem der Kursordner liegen soll, zum Beispiel `Dokumente`.

```bash
git clone https://github.com/faensi/python_basics-nov-2026.git
cd python_basics-nov-2026
```

Wenn GitHub nach einer Anmeldung fragt, melde dich mit deinem GitHub-Konto an. Git Credential Manager speichert diese Anmeldung für den nächsten Abruf.

Danach legst du die Umgebung an, wie in `README.md` beschrieben.

## Neue Kursstände holen

Wenn der Kursordner schon auf dem Rechner liegt, holst du nur die neuen Stände:

```bash
cd python_basics-nov-2026
git pull
```

`git pull` führt die lokalen Dateien und den Stand auf GitHub zusammen. Hast du eine Kursdatei selbst geändert und der Kurs diese Datei ebenfalls, hält Git an und meldet einen Konflikt. Sichere deine Übungsänderungen, bevor du ziehst, wenn du sie behalten willst.
