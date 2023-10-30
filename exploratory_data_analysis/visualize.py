import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column):
    """Plot a histogram for a specific column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=30, kde=True)
    plt.title('Histogram of ' + column)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_boxplot(data, column):
    """Plot a boxplot for a specific column."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data[column])
    plt.title('Boxplot of ' + column)
    plt.xlabel(column)
    plt.show()

def plot_correlation_matrix(data):
    """Plot a correlation matrix for the data."""
    plt.figure(figsize=(12, 10))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
