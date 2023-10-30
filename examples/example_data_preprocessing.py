import pandas as pd
from data_preprocessing.cleaning import remove_missing_values, fill_missing_values
from utils.file_operations import read_csv, write_csv

# Load data
data = read_csv('path_to_your_data.csv')

# Remove columns with more than 50% missing values
cleaned_data = remove_missing_values(data, threshold=0.5)

# Fill missing values with the mean value of each column
filled_data = fill_missing_values(cleaned_data, strategy='mean')

# Save the processed data
write_csv(filled_data, 'path_to_save_cleaned_data.csv')
