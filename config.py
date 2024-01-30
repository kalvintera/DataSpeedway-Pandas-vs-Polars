from pathlib import Path
from dataclasses import dataclass


@dataclass
class Config:
    # Pfaddefinition für .py
    # Hauptverzeichnispfad des Projekts
    project_path = Path(__file__).parent.resolve()

    # Pfad für den Datenordner innerhalb des Projekts
    data_input_path = project_path.joinpath("data")

    # Pfad für den Berichte-Ordner innerhalb des Projekts
    reports_path = project_path.joinpath("reports")
