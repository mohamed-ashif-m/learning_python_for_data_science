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

# Scatter plot
sns.scatterplot(x='feature1', y='feature2', data=data)
plt.title('Feature1 vs Feature2')
plt.show()
plt.clf()

# Correlation heatmap
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
plt.clf()

# Check for missing values
print(data.isnull().sum())

# Fill missing values (example: replacing NaNs with the mean)
data['column_name'].fillna(data['column_name'].mean(), inplace=True)

# Drop missing rows or columns
data.dropna(inplace=True)  # Removes all rows with NaN values
# Mean, Median, Mode
print(f"Mean: {data['column_name'].mean()}")
print(f"Median: {data['column_name'].median()}")
print(f"Mode: {data['column_name'].mode()}")

# Variance and Standard Deviation
print(f"Variance: {data['column_name'].var()}")
print(f"Standard Deviation: {data['column_name'].std()}")

# Create a new feature
data['new_feature'] = data['feature1'] * data['feature2']
# Encode categorical data
data['category_encoded'] = data['category_column'].astype('category').cat.codes
from sklearn.model_selection import train_test_split

# Features and target variable
X = data[['feature1', 'feature2', 'feature3']]
y = data['target']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
import joblib

# Save the model
joblib.dump(model, 'linear_model.pkl')

# Load the model
loaded_model = joblib.load('linear_model.pkl')
# One-Hot Encoding
data = pd.get_dummies(data, columns=['categorical_column'])
# Label Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['encoded_column'] = le.fit_transform(data['categorical_column'])

# Plot a histogram
plt.hist(df['numeric_column'], bins=30, color='blue', alpha=0.7)
plt.title('Histogram of Numeric Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
# Plot a correlation heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
# Boxplot to detect outliers
sns.boxplot(x='category_column', y='numeric_column', data=df)
plt.title('Boxplot of Numeric Column by Category')
plt.show()

width = [8.36, 15.11, 19.92, 8.25]

for index, x in enumerate (width):
  print('Room' + str(index + 1) + ' -', str(x))



