import pandas as pd
from machine_learning.models import train_linear_model, train_random_forest
from machine_learning.evaluation import evaluate_model
from utils.helpers import split_data, train_test_split_data
from utils.file_operations import read_csv

# Load data
data = read_csv('path_to_your_data.csv')

# Split data into features and target
X, y = split_data(data, 'target_column')

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split_data(X, y)

# Train a linear regression model
linear_model = train_linear_model(X_train, y_train)

# Evaluate the linear model
linear_model_eval = evaluate_model(linear_model, X_test, y_test)
print('Linear Model Evaluation:', linear_model_eval)

# Train a random forest regressor
random_forest_model = train_random_forest(X_train, y_train)

# Evaluate the random forest model
random_forest_model_eval = evaluate_model(random_forest_model, X_test, y_test)
print('Random Forest Model Evaluation:', random_forest_model_eval)
