# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("student_data.csv")

# Show first 5 rows
print("\nFIRST 5 ROWS OF DATA:")
print(data.head())

# -----------------------------------
# 1. BAR CHART
# -----------------------------------

plt.figure(figsize=(8,5))
plt.bar(data["Name"], data["Maths"])

plt.title("Maths Marks of Students")
plt.xlabel("Student Names")
plt.ylabel("Maths Marks")

plt.show()

# -----------------------------------
# 2. PIE CHART
# -----------------------------------

attendance = data["Attendance"]

plt.figure(figsize=(7,7))

plt.pie(
    attendance,
    labels=data["Name"],
    autopct='%1.1f%%'
)

plt.title("Attendance Percentage")

plt.show()

# -----------------------------------
# 3. HISTOGRAM
# -----------------------------------

plt.figure(figsize=(8,5))

plt.hist(data["Science"], bins=5)

plt.title("Science Marks Distribution")
plt.xlabel("Science Marks")
plt.ylabel("Frequency")

plt.show()

# -----------------------------------
# 4. SCATTER PLOT
# -----------------------------------

plt.figure(figsize=(8,5))

plt.scatter(data["Maths"], data["Science"])

plt.title("Maths vs Science")
plt.xlabel("Maths Marks")
plt.ylabel("Science Marks")

plt.show()

# -----------------------------------
# 5. HEATMAP
# -----------------------------------

marks_data = data[["Maths", "Science", "English", "Attendance"]]

plt.figure(figsize=(8,5))

sns.heatmap(
    marks_data.corr(),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()