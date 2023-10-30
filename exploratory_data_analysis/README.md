# Exploratory Data Analysis Module

This module provides tools for exploring and understanding your data. It includes functions for visualization, statistical analysis, and correlation analysis.

## Visualization (`visualize.py`)

### Functions:

#### `plot_histogram(data, column)`
- **Description**: Plots a histogram of the specified column.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `column`: A string, the name of the column to plot.
- **Returns**: A matplotlib Axes object.

#### `plot_boxplot(data, column)`
- **Description**: Plots a boxplot of the specified column.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `column`: A string, the name of the column to plot.
- **Returns**: A matplotlib Axes object.

#### `plot_correlation_matrix(data)`
- **Description**: Plots a correlation matrix of the DataFrame.
- **Parameters**:
  - `data`: A pandas DataFrame.
- **Returns**: A matplotlib Axes object.

## Statistics (`statistics.py`)

### Functions:

#### `calculate_summary_statistics(data)`
- **Description**: Calculates and returns summary statistics of the DataFrame.
- **Parameters**:
  - `data`: A pandas DataFrame.
- **Returns**: A pandas DataFrame containing the summary statistics.

#### `calculate_percentiles(data, columns, percentiles=[25, 50, 75])`
- **Description**: Calculates specified percentiles for the given columns of the DataFrame.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `columns`: A list of strings, the names of the columns.
  - `percentiles`: A list of numbers, the percentiles to calculate. Default is [25, 50, 75].
- **Returns**: A pandas DataFrame containing the calculated percentiles.

## Correlation Analysis (`correlation.py`)

### Functions:

#### `calculate_correlation_matrix(data)`
- **Description**: Calculates and returns the correlation matrix of the DataFrame.
- **Parameters**:
  - `data`: A pandas DataFrame.
- **Returns**: A pandas DataFrame containing the correlation matrix.

#### `find_highly_correlated_pairs(data, threshold=0.8)`
- **Description**: Identifies and returns pairs of columns that have a correlation coefficient above the specified threshold.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `threshold`: A float, the correlation coefficient threshold. Default is 0.8.
- **Returns**: A list of tuples, each tuple containing a pair of column names and their correlation coefficient.
