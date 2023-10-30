# Machine Learning Module

This module provides functions for building, evaluating, and making predictions with machine learning models.

## Models (`models.py`)

### Functions:

#### `train_linear_model(features, target)`
- **Description**: Trains a linear regression model.
- **Parameters**:
  - `features`: A pandas DataFrame, the feature variables.
  - `target`: A pandas Series, the target variable.
- **Returns**: A trained linear regression model.

#### `train_lasso_model(features, target, alpha=1.0)`
- **Description**: Trains a Lasso regression model.
- **Parameters**:
  - `features`: A pandas DataFrame, the feature variables.
  - `target`: A pandas Series, the target variable.
  - `alpha`: A float, the regularization strength. Default is 1.0.
- **Returns**: A trained Lasso regression model.

#### `train_ridge_model(features, target, alpha=1.0)`
- **Description**: Trains a Ridge regression model.
- **Parameters**:
  - `features`: A pandas DataFrame, the feature variables.
  - `target`: A pandas Series, the target variable.
  - `alpha`: A float, the regularization strength. Default is 1.0.
- **Returns**: A trained Ridge regression model.

#### `train_decision_tree(features, target, max_depth=None)`
- **Description**: Trains a decision tree regressor.
- **Parameters**:
  - `features`: A pandas DataFrame, the feature variables.
  - `target`: A pandas Series, the target variable.
  - `max_depth`: An integer or None, the maximum depth of the tree. Default is None.
- **Returns**: A trained decision tree regressor.

#### `train_random_forest(features, target, n_estimators=100)`
- **Description**: Trains a random forest regressor.
- **Parameters**:
  - `features`: A pandas DataFrame, the feature variables.
  - `target`: A pandas Series, the target variable.
  - `n_estimators`: An integer, the number of trees in the forest. Default is 100.
- **Returns**: A trained random forest regressor.

## Evaluation (`evaluation.py`)

### Functions:

#### `evaluate_model(model, test_features, test_target)`
- **Description**: Evaluates a trained machine learning model using mean squared error, R^2 score, and mean absolute error.
- **Parameters**:
  - `model`: A trained machine learning model.
  - `test_features`: A pandas DataFrame, the feature variables for testing.
  - `test_target`: A pandas Series, the target variable for testing.
- **Returns**: A dictionary containing the evaluation metrics.

#### `cross_validate_model(model, features, target, cv=5)`
- **Description**: Performs cross-validation on a machine learning model.
- **Parameters**:
  - `model`: A machine learning model (not necessarily trained).
  - `features`: A pandas DataFrame, the feature variables.
  - `target`: A pandas Series, the target variable.
  - `cv`: An integer, the number of cross-validation folds. Default is 5.
- **Returns**: A dictionary containing the cross-validation results.

## Prediction (`prediction.py`)

### Functions:

#### `make_predictions(model, new_data)`
- **Description**: Uses a trained machine learning model to make predictions on new data.
- **Parameters**:
  - `model`: A trained machine learning model.
  - `new_data`: A pandas DataFrame, the new data for making predictions.
- **Returns**: A numpy array containing the predictions.
