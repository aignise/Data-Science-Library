import pandas as pd

def read_csv(file_path):
    """Read data from a CSV file."""
    return pd.read_csv(file_path)

def write_csv(data, file_path):
    """Write data to a CSV file."""
    data.to_csv(file_path, index=False)
