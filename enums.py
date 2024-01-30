import enum


class ReadOperationType(enum.Enum):
    # Enum für verschiedene Leseoperationen mit Polars
    read_data_polars_lazy = "read_data_polars_lazy"


class FilterOperationType(enum.Enum):
    # Enum für verschiedene Filteroperationen mit Pandas und Polars
    filter_data_pandas = "filter_data_pandas"
    filter_data_polars = "filter_data_polars"
    filter_data_with_scan = "filter_data_scan"
