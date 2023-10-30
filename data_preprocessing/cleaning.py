import pandas as pd

def remove_missing_values(data, threshold=0.5):
    """Remove columns with missing values exceeding the threshold."""
    return data.dropna(axis=1, thresh=int((1 - threshold) * data.shape[0]))

def fill_missing_values(data, strategy='mean'):
    """Fill missing values using a specific strategy ('mean', 'median', 'mode')."""
    if strategy == 'mean':
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'mode':
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Invalid strategy. Use 'mean', 'median', or 'mode'.")

def remove_outliers(data, columns, threshold=1.5):
    """Remove outliers from specified columns using the IQR method."""
    for col in columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        data = data[(data[col] >= (Q1 - threshold * IQR)) & (data[col] <= (Q3 + threshold * IQR))]
    return data

def encode_categorical_data(data):
    """Encode categorical variables using one-hot encoding."""
    return pd.get_dummies(data, drop_first=True)
