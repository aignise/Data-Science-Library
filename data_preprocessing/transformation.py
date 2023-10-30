import pandas as pd
import numpy as np
from scipy.stats import boxcox

def log_transform(data, columns):
    """Apply log transformation to specified columns."""
    data = data.copy()
    data[columns] = np.log1p(data[columns])
    return data

def square_root_transform(data, columns):
    """Apply square root transformation to specified columns."""
    data = data.copy()
    data[columns] = np.sqrt(data[columns])
    return data

def box_cox_transform(data, column):
    """Apply Box-Cox transformation to a specified column."""
    data = data.copy()
    data[column], _ = boxcox(data[column] + 1)  # Adding 1 to avoid issues with 0 values
    return data
