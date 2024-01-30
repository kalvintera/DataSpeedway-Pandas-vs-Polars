<p align="center">
<img src="content/logo.png" alt="Girl in a jacket" 
width="500" height="500">

</p>


# Performancevergleich: Pandas vs. Polars

## Inhaltsverzeichnis
1. [Einleitung](#einleitung)
   - [Einleitung zu Pandas](content/Pandas-Introduction.md)
   - [Einleitung zu Polars](content/Polars-Introduction.md)
2. [Projekteinrichtung](#projekteinrichtung)
3. [Detaillierte Paketbeschreibung](#detaillierte-paketbeschreibung)
4. [Verwendung des Projekts](#verwendung-des-projekts)
5. [Anwendungsfälle](#anwendungsfälle)
6. [Comparative-Analysis Notebook](#comparative-analysis-notebook)
7. [Lizenz und Datenquellen](#lizenz-und-datenquellen)
8. [Mitwirkung](#mitwirkung)


## Einleitung
In der sich rasant entwickelnden Welt der Datenwissenschaft ist die Fähigkeit, große Datensätze effizient zu verarbeiten, entscheidend. Unser Projekt "Performancevergleich: Pandas vs. Polars" bietet eine umfassende Analyse und einen Vergleich dieser beiden führenden Datenverarbeitungs-Bibliotheken. Wir konzentrieren uns auf den Umgang mit großen Datasets (2 GB und 4 GB), um die Leistungsunterschiede klar aufzuzeigen. Dieses Repository dient als Lehrmaterial und Referenz für Data Science-Studenten und Fachleute, die die optimale Bibliothek für ihre spezifischen Anwendungsfälle auswählen möchten.

## Projekteinrichtung
### Setup mit Pipenv
```bash
cd project_directory

pipenv install
```

### Detaillierte Paketbeschreibung
- `pandas`: Eine umfassende Datenmanipulationsbibliothek, die eine Vielzahl von Funktionen für die Bearbeitung und Analyse von Datenstrukturen wie DataFrames und Serien bietet.
- `polars`: Eine schnelle Datenverarbeitungsbibliothek, optimiert für große Datenmengen und entwickelt, um Operationen effizient und parallel auszuführen.
- `ydata-profiling`: Erstellt detaillierte Datenberichte und bietet umfassende Analysemöglichkeiten für Datenexploration und -visualisierung.
- `nltk`: Ein Toolkit für natürliche Sprachverarbeitung, das insbesondere für die Entfernung von Stopwörtern und Textdatenbereinigung verwendet wird.
- `pygwalker`: Bietet interaktive Lern- und Erkundungsmöglichkeiten für Benutzer, ideal für das Experimentieren mit verschiedenen Datenoperationen.
- `typer`: Ermöglicht die Erstellung von benutzerfreundlichen Kommandozeileninterfaces, was die Bedienung und Nutzung von Skripten erleichtert.

### Unterstützende Bibliotheken
- `rich`: Eine Bibliothek, die reichhaltige Text- und Formatierungsfunktionen in der Konsole bereitstellt, ideal für die ansprechende Darstellung von Daten und Ergebnissen.
- `ipywidgets`: Bietet interaktive HTML-Widgets für Jupyter Notebooks, die die Interaktion mit Daten in Notebooks verbessern.
- `numpy`: Eine fundamentale Bibliothek für wissenschaftliches Rechnen in Python, unerlässlich für die Handhabung von Arrays und mathematischen Operationen.
- `notebook`: Ermöglicht die Entwicklung und Präsentation von Jupyter Notebooks, ein wesentliches Werkzeug für die Darstellung von Datenanalysen und -visualisierungen.

## Verwendung des Projekts
### Ausführen der Skripte

```bash
pipenv shell
python main.py --help
```

Dies zeigt die verfügbaren CLI-Befehle an. 
Die wichtigsten Befehle sind:

- `run_read_test_pandas`: Führt einen Lesevorgang mit Pandas aus.
- `run_read_test_polars`: Führt einen Lesevorgang mit Polars aus.
- `compare_filter_operations`: Vergleicht Filteroperationen zwischen Pandas und Polars.

```bash

python main.py run_read_test_pandas
python main.py run_read_test_polars
python main.py compare_filter_operations
```

> ### Was sind CLI-Befehle?
>CLI-Befehle (Command Line Interface Befehle) sind Anweisungen, die über ein Terminal oder eine Befehlszeilenschnittstelle ausgeführt werden. Sie ermöglichen es Benutzern, mit einem Programm oder Betriebssystem durch Eingabe von Textbefehlen zu interagieren, anstatt eine grafische Benutzeroberfläche zu verwenden.

>### Verwendung von Typer
>In diesem Projekt wurde `Typer` verwendet, ein leistungsfähiges Paket für die Erstellung von CLI-Anwendungen in Python. Typer erleichtert das Erstellen von Befehlszeilenschnittstellen, indem es die Definition von Befehlen und Argumenten vereinfacht und gleichzeitig eine automatische Hilfe-Seite und Typüberprüfungen bietet.

>### Anwendungsfälle für Typer
>CLI-Pakete wie Typer werden häufig in folgenden Szenarien verwendet:

>- **Automatisierung von Aufgaben:** Für Skripte und Anwendungen, die regelmäßig ausgeführt werden müssen, wie Datenmigrationen, Backups oder Batchverarbeitungen.
>- **Werkzeuge für Entwickler:** Zur Erstellung von Entwicklerwerkzeugen, die über das Terminal verwendet werden, wie Versionskontrollsysteme, Testwerkzeuge oder Deployment-Skripte.
>- **Server-Management:** Für Aufgaben im Zusammenhang mit der Verwaltung von Servern und Infrastruktur, zum Beispiel Starten und Stoppen von Diensten oder Überwachen von Systemressourcen.
>- **Datenwissenschaft und -analyse:** Zum Ausführen von Datenverarbeitungsaufgaben, insbesondere wenn große Datensätze oder komplexe Berechnungen beteiligt sind, die auf einem entfernten Server oder in einer Umgebung ohne grafische Benutzeroberfläche ausgeführt werden müssen.

>Typer bietet eine saubere, intuitive und leicht erweiterbare Möglichkeit, CLI-Befehle für diese und viele andere Aufgaben zu definieren.

>#### Beispiel für einen Typer-Befehl:
```python
import typer

app = typer.Typer()

@app.command()
def my_command(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    app()
```


### CLI-Befehl: `compare_filter_operations`

Der `compare_filter_operations` Befehl ist für den Vergleich von Filteroperationen zwischen Pandas und Polars konzipiert. Dieser Befehl führt eine Reihe von Operationen durch, um die Effizienz und Geschwindigkeit der beiden Bibliotheken bei der Durchführung von Filteraufgaben zu analysieren. Hier sind die spezifischen Aktionen, die durch diesen Befehl ausgeführt werden:

1. **Filtern mit Pandas:**
   - Liest zunächst eine CSV-Datei mit Pandas ein.
   - Führt dann Filteroperationen auf dem DataFrame aus. Dies beinhaltet das Filtern von Daten basierend auf spezifischen Kriterien, wie in Ihrem Code definiert.

2. **Filtern mit Polars:**
   - Liest die gleiche CSV-Datei mit Polars ein.
   - Führt ähnliche Filteroperationen wie bei Pandas durch, jedoch unter Verwendung der Polars-Bibliothek.

3. **Vergleich der Leistungsdaten:**
   - Misst und vergleicht die Zeit, die für die Durchführung der Filteroperationen mit beiden Bibliotheken benötigt wird.
   - Dies hilft dabei, die Effizienz von Pandas und Polars in Bezug auf Zeit und Speicherressourcen bei der Datenfilterung zu beurteilen.

Der Befehl ist besonders nützlich, um zu verstehen, welche Bibliothek in bestimmten Filterszenarien besser performt, insbesondere bei großen Datenmengen.

#### Anwendung des Befehls:
Um diesen Befehl auszuführen, geben Sie im Terminal folgendes ein:
```bash
python main.py compare_filter_operations
```

Experimente können über `main.py` oder das Jupyter Notebook `Comparative-Analysis.ipynb` durchgeführt werden.

## Anwendungsfälle
In diesem Projekt wird analysiert, wie Pandas und Polars sich bei verschiedenen Datenoperationen verhalten, insbesondere in Bezug auf:

- **Lesevorgänge**: Beurteilung der Geschwindigkeit und Effizienz beim Einlesen großer Datensätze.
- **Filteroperationen**: Vergleich der Leistung bei komplexen Filterbedingungen.
- **Datenbereinigung**: Effizienz bei der Entfernung von Stopwörtern und anderen Textbereinigungsprozessen.
- **Datenreporting**: Erstellung von Datenprofilen und Visualisierungen zur Analyse.

Diese Anwendungsfälle sind besonders relevant für Szenarien mit großen Datenmengen, wo die Performance von entscheidender Bedeutung ist.

## Comparative-Analysis Notebook
Das `Comparative-Analysis.ipynb` Notebook ist ein zentraler Bestandteil dieses Projekts. In diesem Notebook wird die Leistung zwischen den beiden Datenverarbeitungspaketen Pandas und Polars verglichen. Die Bewertung konzentriert sich auf Schlüsseloperationen wie das Einlesen von Daten (`reading`), Filtern (`filtering`) und Aggregieren (`aggregation`). 

#### CPU-Zeit vs. Wall Time
- **CPU-Zeit** bezieht sich auf die tatsächliche Zeit, die der Prozessor für die Ausführung des Codes benötigt. Diese Zeit kann länger sein als die Wall Time, insbesondere wenn die Prozesse auf mehrere Kerne verteilt sind.
- **Wall Time**, auch bekannt als Elapsed Time, ist die tatsächliche Zeit vom Start bis zum Ende der Ausführung des Codes, wie sie von einer Uhr gemessen wird. 

In Szenarien, in denen mehrere Prozesse oder Threads gleichzeitig ausgeführt werden, kann die CPU-Zeit länger sein als die Wall Time, da mehrere Kerne gleichzeitig an unterschiedlichen Teilen des Codes arbeiten. Die `%time` Methode gibt beide Zeiten aus, um einen umfassenden Einblick in die Performance des Codes zu geben.
### Pygwalker und YData
Zusätzlich zu diesen Leistungsvergleichen werden in diesem Notebook zwei wichtige Pakete vorgestellt: `pygwalker` und `ydata`.

#### Pygwalker
`Pygwalker` ist ein interaktives Lernwerkzeug, das hilft, komplexe Datenstrukturen und Algorithmen spielerisch zu verstehen. Es wird in folgenden Szenarien verwendet:
- **Bildung:** Ideal für Lehrkräfte und Studenten, um Programmierkonzepte in einer interaktiven Umgebung zu demonstrieren und zu lernen.
- **Datenexploration:** Hilfreich für Datenwissenschaftler, um Datenstrukturen und Algorithmen visuell zu erkunden und zu verstehen.

#### YData
`YData` ist ein leistungsfähiges Paket für Datenprofiling und -analyse. Es wird in folgenden Bereichen eingesetzt:
- **Datenqualitätsbewertung:** Ermöglicht es Datenwissenschaftlern und Analysten, schnell Einblicke in die Qualität und Struktur ihrer Daten zu gewinnen.
- **Explorative Datenanalyse:** Bietet umfangreiche Funktionen zur visuellen Darstellung und Zusammenfassung von Daten, was die Hypothesenbildung und das Erkennen von Mustern unterstützt.

### Nutzung des Notebooks
Das Notebook bietet eine umfassende Anleitung und Beispiele für die Nutzung von `pygwalker` und `ydata` sowie den Vergleich zwischen Pandas und Polars. Es ist so gestaltet, dass Benutzer die verschiedenen Aspekte der Datenverarbeitung und -analyse praktisch nachvollziehen können.

#### Ausführen des Notebooks
Um das Notebook zu verwenden, öffnen Sie es in JupyterLab oder Jupyter Notebook und folgen Sie den Anweisungen und Beispielen.


## Lizenz und Datenquellen
### Lizenz
Die Lizenzbestimmungen für die Daten richten sich nach den Quellen (Kaggle, etc.). Der Code steht unter einer MIT-Lizenz.

### Quellen
- Kaggle-Datasets: 
  - [Anime Dataset 2023](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset/data?select=final_animedataset.csv)
  - [Anime Recommendation Database 2020](https://www.kaggle.com/code/fahadbinahmed/anime-recommendation-system-cf/input?select=animelist.csv)
  - [Linkedin Canada: Data Science Jobs 2024](https://www.kaggle.com/datasets/kanchana1990/linkedin-canada-data-science-jobs-2024?select=linkedin_canada.csv)
  - [Bike Sharing in Washington D.C. Dataset](https://www.kaggle.com/datasets/marklvl/bike-sharing-dataset)

## Mitwirkung
Benutzer sind eingeladen, das Repository zu forken, Issues zu erstellen und zur Weiterentwicklung des Projekts beizutragen.