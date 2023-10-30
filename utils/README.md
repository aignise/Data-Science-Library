# Utilities Module

This module contains utility functions that support various operations of the data analysis library, including data splitting, logging, and file operations.

## Data Splitting (`helpers.py`)

### Functions:

#### `split_data(data, target_column)`
- **Description**: Splits the dataset into features (X) and target (y) based on the target column.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `target_column`: A string, the name of the target variable column.
- **Returns**: Two pandas DataFrames, the features (X) and the target (y).

#### `train_test_split_data(X, y, test_size=0.2, random_state=42)`
- **Description**: Splits the dataset into training and test sets.
- **Parameters**:
  - `X`: A pandas DataFrame, the feature variables.
  - `y`: A pandas Series or DataFrame, the target variable.
  - `test_size`: A float, the proportion of the dataset to include in the test split. Default is 0.2.
  - `random_state`: An int, random_state is the seed used by the random number generator. Default is 42.
- **Returns**: Four pandas DataFrames/Series, X_train, X_test, y_train, y_test.

## Logging (`logger.py`)

### Functions:

#### `configure_logging(level=logging.INFO)`
- **Description**: Configures the logging settings for the library.
- **Parameters**:
  - `level`: The root logger level. Defaults to logging.INFO.
- **Returns**: None.

#### `log_message(message, level=logging.INFO)`
- **Description**: Logs a message at the specified log level.
- **Parameters**:
  - `message`: A string, the log message.
  - `level`: The log level for this message. Defaults to logging.INFO.
- **Returns**: None.

## File Operations (`file_operations.py`)

### Functions:

#### `read_csv(file_path)`
- **Description**: Reads data from a CSV file.
- **Parameters**:
  - `file_path`: A string, the path to the CSV file.
- **Returns**: A pandas DataFrame.

#### `write_csv(data, file_path)`
- **Description**: Writes data to a CSV file.
- **Parameters**:
  - `data`: A pandas DataFrame.
  - `file_path`: A string, the path where to save the CSV file.
- **Returns**: None.
