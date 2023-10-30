import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(data, target_column):
    """Split data into features and target based on target column."""
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return X, y

def train_test_split_data(X, y, test_size=0.2, random_state=42):
    """Split data into training and test sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
