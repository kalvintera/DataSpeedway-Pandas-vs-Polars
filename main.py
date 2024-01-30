import gc
from timeit import default_timer as timer
import typer
from typing import Optional
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich import print
import pandas as pd
import polars as pl
from enums import ReadOperationType, FilterOperationType
from comparative_analysis import ComparePackages

# CLI-Package Typer Dokumentation: https://typer.tiangolo.com/
app = typer.Typer()
compare = ComparePackages()


@app.command()
def run_read_test_pandas():
    # Sammeln und Beseitigen von nicht genutztem Speicher
    gc.collect()

    # Fortschrittsanzeige für das Lesen mit Pandas
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task(description="Reading with Pandas...", total=None)
        gc.collect()

        # Testfunktion für das Lesen großer CSV-Dateien mit Pandas
        compare.read_large_csv_pandas_test(file_name="final_animedataset")
        progress.update(task, advance=1)
        progress.remove_task(task_id=progress.task_ids[0])


@app.command()
def run_read_test_polars(
    operation_type: Optional[ReadOperationType] = typer.Argument(default=None),
):
    # Fortschrittsanzeige für das Lesen mit Polars
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        if operation_type == ReadOperationType.read_data_polars_lazy:
            # Lesen im Lazy-Modus mit Polars
            task = progress.add_task(
                description="Reading with Polars (Lazy)...", total=None
            )
            compare.read_large_csv_polars_lazy(file_name="final_animedataset")
            progress.update(task, advance=1)
            progress.remove_task(task_id=progress.task_ids[0])
            gc.collect()
        else:
            # Lesen im Eager-Modus mit Polars
            gc.collect()
            task = progress.add_task(
                description="Reading with Polars (Eager)...", total=None
            )
            compare.read_large_csv_polars_test(file_name="final_animedataset")
            progress.update(task, advance=1)
            progress.remove_task(task_id=progress.task_ids[0])
            gc.collect()


@app.command()
def compare_filter_operations(operation_type: FilterOperationType):
    # Fortschrittsanzeige für Filteroperationen
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        gc.collect()

        if operation_type == FilterOperationType.filter_data_pandas:
            # Filtern mit Pandas
            task = progress.add_task(description="Reading with Pandas...", total=None)
            test_pandas = pd.read_csv(
                compare.config.data_input_path.joinpath(
                    compare.config.large_data_for_reading_comparison + ".csv"
                )
            )
            progress.update(task, advance=1)
            progress.remove_task(task_id=progress.task_ids[0])
            print("\n", "[bold green]filtering data with pandas...[/bold green]")
            start = timer()
            compare.filter_data(
                test_pandas, column_1="type", column_2="score", value="Movie", value_2=8
            )
            end = timer()
            print(f"Pandas [bold red]filter time: {end - start}[/bold red]", "\n")
        elif operation_type == FilterOperationType.filter_data_polars:
            # Filtern mit Polars
            gc.collect()
            task = progress.add_task(description="Reading with Polars...", total=None)
            test_polars = pl.read_csv(
                compare.config.data_input_path.joinpath(
                    compare.config.large_data_for_reading_comparison + ".csv"
                )
            )
            progress.update(task, advance=1)
            progress.remove_task(task_id=progress.task_ids[0])
            print("[bold green]filtering data with polars[/bold green]...")
            start = timer()
            compare.filter_data(
                test_polars, column_1="type", column_2="score", value="Movie", value_2=8
            )
            end = timer()
            print(f"Polars [bold red]filter time: {end - start}")
        elif operation_type == FilterOperationType.filter_data_with_scan:
            # Filtern mit Polars und Scan CSV
            print(
                "[bold green]filtering data with polars with scan_csv [/bold green]..."
            )
            start = timer()
            test_polars_scan = compare.filter_data_with_scan(
                file_name=compare.config.large_data_for_reading_comparison,
                column_1="type",
                column_2="score",
                value="Movie",
                value_2=8,
            )
            end = timer()
            print(f"Polars filter with scan time: {end - start}")
            print(f"Polars [bold red]filter time: {end - start}")


if __name__ == "__main__":
    app()
