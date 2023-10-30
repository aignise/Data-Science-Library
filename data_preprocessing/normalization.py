import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

def min_max_scaling(data):
    """Apply min-max scaling to the data."""
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    return pd.DataFrame(scaled_data, columns=data.columns)

def standardization(data):
    """Standardize the data (zero mean and unit variance)."""
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)
    return pd.DataFrame(standardized_data, columns=data.columns)

def robust_scaling(data):
    """Apply robust scaling (using median and interquartile range)."""
    scaler = RobustScaler()
    robust_scaled_data = scaler.fit_transform(data)
    return pd.DataFrame(robust_scaled_data, columns=data.columns)
