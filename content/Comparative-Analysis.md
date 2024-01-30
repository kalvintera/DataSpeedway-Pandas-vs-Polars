# Comparative Analysis of Pandas and Polars

## Introduction
This section provides a comparative analysis of Pandas and Polars, two powerful data manipulation libraries. We'll compare their performance, ease of use, and functionality with code examples and discuss where each library excels.
- [View the Comparative Analysis Notebook](./notebooks/Comparative-Analysis.ipynb)
## Performance Comparison
Here we compare the performance of Pandas and Polars in handling large datasets.

### Reading Large Datasets

This code uses time.time() to get the current time before and after the operation, 
then calculates the difference to find out how long the operation took.
```python
import pandas as pd
import polars as pl


# create read statements
print("Pandas read time: ")
%time read_pandas = pd.read_csv('large_dataset.csv')
print("-----------", "\n")
print("read time for polars: ")
%time read_polars = pl.read_csv('large_dataset.csv')
```

### Memory Usage Analysis

#### Objective
To compare how Pandas and Polars manage memory, particularly when handling large datasets. This comparison will help us understand which library is more efficient in terms of memory usage for data-intensive tasks.

Setup for Memory Profiling
Before starting, ensure you have the memory_profiler module installed. If not, you can install it using pip:

```bash
pipenv install memory_profiler
```
Then, you can use the `%load_ext` magic command in your Jupyter Notebook to load the memory profiler:

```jupyter
%load_ext memory_profiler
```
