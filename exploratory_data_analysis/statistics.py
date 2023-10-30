import pandas as pd

def calculate_summary_statistics(data):
    """Calculate summary statistics (mean, median, mode, etc.)."""
    return data.describe(include='all')

def calculate_percentiles(data, columns, percentiles=[25, 50, 75]):
    """Calculate specific percentiles for given columns."""
    return data[columns].quantile(q=[p / 100 for p in percentiles])
