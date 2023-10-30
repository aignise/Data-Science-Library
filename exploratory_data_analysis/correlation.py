import pandas as pd

def calculate_correlation_matrix(data):
    """Calculate a correlation matrix for the data."""
    return data.corr()

def find_highly_correlated_pairs(data, threshold=0.8):
    """Find pairs of columns with correlation above a certain threshold."""
    corr_matrix = data.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
    return data[to_drop]
