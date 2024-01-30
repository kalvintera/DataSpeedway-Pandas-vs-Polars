import os
from timeit import default_timer as timer
import pandas as pd
import polars as pl
from rich import print
from config import Config


class ComparePackages:
    def __init__(self):
        self.config = Config()

    def _create_file_path_with_info(self, file_name: str):
        file_path = self.config.data_input_path.joinpath(file_name + ".csv")
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

        print(f"File size: {file_size_mb:.2f} MB")
        return file_path

    def read_large_csv_pandas_test(self, file_name: str):
        file_path = self._create_file_path_with_info(file_name=file_name)

        # Pandas
        start = timer()
        pandas_df = pd.read_csv(file_path)
        end = timer()
        print(f"Pandas read time: [bold red]{end - start}[/bold red] seconds")
        print(
            f"Pandas memory usage: [bold red]{pandas_df.memory_usage(deep=True).sum() / (1024 * 1024)}[/bold red] MB",
            "\n",
        )

    def read_large_csv_polars_test(self, file_name: str):
        file_path = self._create_file_path_with_info(file_name=file_name)
        # Polars
        start = timer()
        polars_df = pl.read_csv(file_path)
        end = timer()
        print(f"Polars read time: [bold red]{end - start}[/bold red] seconds")
        print(
            f"Polars memory size:[bold red] {polars_df.estimated_size(unit='mb')}[/bold red] MB"
        )

    def read_large_csv_polars_lazy(self, file_name: str):
        file_path = self._create_file_path_with_info(file_name=file_name)
        # Polars
        start = timer()
        polars_df = pl.scan_csv(file_path)
        end = timer()
        print(f"Polars read time: [bold red]{end - start}[/bold red] seconds")

    @staticmethod
    def filter_data(df, column_1: str, value: str, column_2: str, value_2: int):
        if isinstance(df, pd.DataFrame):
            return df[(df[column_1] == value) & (df[column_2] > value_2)]
        else:
            return (
                df.lazy()
                .filter((pl.col(column_1) == value) & (pl.col(column_2) > value_2))
                .collect()
            )

    def filter_data_with_scan(
        self, file_name, column_1: str, value: str, column_2: str, value_2: int
    ):
        if file_name:
            file_path = self._create_file_path_with_info(file_name=file_name)
            # Use pl.scan_csv to create a LazyFrame
            polars_scan_df = pl.scan_csv(file_path)

            # Apply filter using filter() method
            filtered_df = polars_scan_df.filter(
                (pl.col(column_1) == value) & (pl.col(column_2) > value_2)
            )

            # Collect the results into a DataFrame
            return filtered_df.collect()
        else:
            raise RuntimeError("File name is not provided")


if __name__ == "__main__":
    compare = ComparePackages()
    pd_df = compare.read_large_csv_pandas_test
    input("Waiting ...")
