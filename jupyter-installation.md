# Jupyter und die Notebook-Ansicht in Spyder


Alles hier läuft in der normalen **Miniforge Prompt**, nicht als Administrator. Die Prompt startet in deinem Benutzerordner. `Documents` ist von dort aus der relative Pfad.

Die Paketliste steht in `environment.yml` (inkl. Spyder, Jupyter, Notebook und `spyder-notebook`). Ein separater `conda install` für das Notebook-Plugin ist nicht nötig.

## 0. Install Miniforge prompt aus dem Software-Center

## 1. Miniforge Prompt öffnen

Nicht „Als Administrator ausführen“.

## 2. Proxy setzen (nur im PTB-Netz)

Ohne Proxy schlagen Downloads von conda-forge oft fehl. Die Variablen gelten nur für dieses Prompt-Fenster:

```bat
set HTTPS_PROXY=http://webproxy.bs.ptb.de:8080/
set HTTP_PROXY=http://webproxy.bs.ptb.de:8080/
```

## 3. In den Kursordner wechseln

Der Pfad ist ggf. ein anderer, je nach Ordner in dem unser Projekt sitzt.

```bat
cd Documents\Python-Seminar\python_basics-nov-2026
pwd
```

## 4. Umgebung anlegen oder aktualisieren

**Neu anlegen** (Umgebung `python_grundlagen` existiert noch nicht):

```bat
conda env create -f environment.yml
```

**Aktualisieren** (Umgebung gibt es schon, z. B. nach Änderungen an `environment.yml`):

```bat
conda env update -n python_grundlagen -f environment.yml --prune
```

`--prune` entfernt Pakete, die nicht mehr in der Datei stehen. Damit kommen Python 3.13, Spyder, Jupyter, Notebook, `spyder-notebook`, der Kernel und die Kursbibliotheken.

Die passende Plugin-Fassung von `spyder-notebook` verlangt Spyder 6.1 und Notebook 7.4. Conda setzt die Versionen dafür. Eine Meldung, dass Spyder dabei auf 6.1 bleibt, ist in Ordnung.

## 5. Umgebung aktivieren

```bat
conda activate python_grundlagen
```

## 6. Kernel für Jupyter registrieren

Einmalig (oder erneut nach Neuaufbau der Umgebung). Schreibt in dein Benutzerprofil, keine Administratorrechte nötig:

```bat
python -m ipykernel install --user --name python_grundlagen --display-name "Python Grundlagen"
```

## 7. Jupyter im Browser prüfen

Der Befehl bleibt in diesem Fenster. Beende ihn mit Strg+C:

```bat
jupyter notebook
```

## 8. Spyder starten (optional)

Aus derselben Prompt, nicht über das Spyder aus dem Softwarekatalog:

```bat
spyder
```

In Spyder: **View**, **Panes**, **Notebook**. Die Notebooks des Kurses liegen unter `tag1` bis `tag4`. Die Skripte startest du weiter mit F5. Das Arbeitsverzeichnis bleibt `python_basics-nov-2026`.

## Kurzüberblick

| Schritt | Befehl |
| ------- | ------ |
| Proxy (PTB) | `set HTTPS_PROXY=...` / `set HTTP_PROXY=...` |
| Ordner | `cd Documents\Python-Seminar\python_basics-nov-2026` |
| Neu | `conda env create -f environment.yml` |
| Update | `conda env update -n python_grundlagen -f environment.yml --prune` |
| Aktivieren | `conda activate python_grundlagen` |
| Kernel | `python -m ipykernel install --user --name python_grundlagen --display-name "Python Grundlagen"` |
| Test | `jupyter notebook` bzw. `spyder` |

## Nicht als Administrator

Umgebung, Plugin, Kernel und beide Programme schreiben in dein Benutzerprofil. Startest du die Prompt als Administrator, legt Jupyter den Ordner `AppData\Roaming\jupyter\runtime` so an, dass dein normaler Benutzer dort nicht schreiben darf. Spyder meldet dann, die IPython-Konsole könne nicht starten. Als Administrator zu starten behebt das nur scheinbar.

## Nur wenn diese Meldung schon da ist

Spyder schließen. In der normalen Prompt:

```bat
rmdir /s /q "%APPDATA%\jupyter\runtime"
mkdir "%APPDATA%\jupyter\runtime"
```

Kommt „Zugriff verweigert“, muss jemand mit Administratorrechten einmal den Ordner des Kursteilnehmers freigeben, mit dessen echtem Benutzernamen, nicht aus einer Admin-Prompt mit `%APPDATA%`:

```bat
icacls "C:\Users\NAME\AppData\Roaming\jupyter" /grant "NAME:(OI)(CI)M" /T
```

Danach wieder die normale Miniforge Prompt verwenden und bei Schritt 8 weitermachen.
