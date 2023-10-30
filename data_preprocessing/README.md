# Data Preprocessing Module

This module is dedicated to preparing your dataset for analysis or machine learning models. It provides functions for cleaning, transforming, and normalizing your data.

## Cleaning (`cleaning.py`)

### Functions:

#### `remove_missing_values(data, threshold=0.5)`
- **Description**: Removes columns from the DataFrame that have a proportion of missing values greater than the specified threshold.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `threshold`: A float, the threshold for removing columns with missing values. Default is 0.5.
- **Returns**: A pandas DataFrame with columns having missing values less than the threshold.

#### `fill_missing_values(data, strategy='mean')`
- **Description**: Fills the missing values in the DataFrame using a specified strategy.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `strategy`: A string, the strategy for filling missing values ('mean', 'median', 'mode'). Default is 'mean'.
- **Returns**: A pandas DataFrame with missing values filled.

#### `remove_outliers(data, columns, threshold=1.5)`
- **Description**: Removes the outliers from the specified columns of the DataFrame using the IQR method.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `columns`: A list of strings, the names of the columns from which to remove outliers.
  - `threshold`: A float, the IQR scaling factor to use for defining outliers. Default is 1.5.
- **Returns**: A pandas DataFrame with outliers removed.

#### `encode_categorical_data(data)`
- **Description**: Applies one-hot encoding to the categorical variables in the DataFrame.
- **Parameters**:
  - `data`: A pandas DataFrame.
- **Returns**: A pandas DataFrame with categorical variables one-hot encoded.

## Transformation (`transformation.py`)

### Functions:

#### `log_transform(data, columns)`
- **Description**: Applies a log transformation (natural logarithm) to the specified columns of the DataFrame.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `columns`: A list of strings, the names of the columns to log-transform.
- **Returns**: A pandas DataFrame with log-transformed values in the specified columns.

#### `square_root_transform(data, columns)`
- **Description**: Applies a square root transformation to the specified columns of the DataFrame.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `columns`: A list of strings, the names of the columns to square root-transform.
- **Returns**: A pandas DataFrame with square root-transformed values in the specified columns.

#### `box_cox_transform(data, column)`
- **Description**: Applies a Box-Cox transformation to a specified column of the DataFrame.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `column`: A string, the name of the column to Box-Cox transform.
- **Returns**: A pandas DataFrame with the Box-Cox transformed column.

## Normalization (`normalization.py`)

### Functions:

#### `min_max_scaling(data)`
- **Description**: Applies min-max scaling to the DataFrame, scaling the values to a range of [0, 1].
- **Parameters**:
  - `data`: A pandas DataFrame.
- **Returns**: A pandas DataFrame with values scaled to [0, 1].

#### `standardization(data)`
- **Description**: Standardizes the DataFrame, transforming the values to have a mean of 0 and a standard deviation of 1.
- **Parameters**:
  - `data`: A pandas DataFrame.
- **Returns**: A pandas DataFrame with standardized values.

#### `robust_scaling(data)`
- **Description**: Applies robust scaling to the DataFrame, using the median and the interquartile range for scaling. This is useful for datasets with outliers.
- **Parameters**:
  - `data`: A pandas DataFrame.
- **Returns**: A pandas DataFrame with robustly scaled values.
