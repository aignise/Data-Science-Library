import pandas as pd
from exploratory_data_analysis.visualize import plot_histogram, plot_boxplot
from exploratory_data_analysis.statistics import calculate_summary_statistics
from utils.file_operations import read_csv

# Load data
data = read_csv('path_to_your_data.csv')

# Visualize the distribution of a specific column
plot_histogram(data, 'column_name')

# Create a boxplot for a specific column
plot_boxplot(data, 'column_name')

# Calculate summary statistics
summary_stats = calculate_summary_statistics(data)
print(summary_stats)
