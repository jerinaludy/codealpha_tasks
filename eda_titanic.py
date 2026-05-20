import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Display first 5 rows
print(df.head())
print("\nDataset Information:")
print(df.info())

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
plt.figure(figsize=(8,5))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Gender vs Survival")
plt.show()
sns.countplot(x='Pclass', data=df)
plt.title("Passenger Class Distribution")
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df['Age'].dropna(), bins=30)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.show()
survival_rate = df.groupby('Sex')['Survived'].mean()

print("\nSurvival Rate by Gender:")
print(survival_rate)
print("\nFINAL INSIGHTS:")
print("1. Female passengers survived more.")
print("2. First-class passengers survived more.")
print("3. Missing values exist in Age and Cabin.")
print("4. Fare has outliers.")
print("5. Most passengers are between 20–40 age.")