import numpy as np          # For numerical operations
import pandas as pd         # For data manipulation and analysis
import matplotlib.pyplot as plt  # For data visualization
import seaborn as sns       # For advanced visualizations

# Configure plots
plt.style.use('ggplot')
sns.set_theme()

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Display the first few rows
print(data.head())

# Basic information about the dataset
print(data.info())

# Summary statistics
print(data.describe())

# Distribution of a variable
sns.histplot(data['column_name'], kde=True)
plt.title('Distribution of Column')
plt.show()
plt.clf()


