import pandas as pd

# `None` in a numeric column is coerced to `NaN` (Not a Number) by Pandas
data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82],
}

df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df)

# .isnull() produces a boolean mask; .sum() counts True (missing) values per column
print("\nMissing Values:")
print(df.isnull().sum())

# Impute missing entries with column mean (.mean() skips NaNs by default)
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Drops exact duplicate rows (returns a new DataFrame unless inplace=True)
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

# Summary stats (count, mean, std, min, quartiles, max) for numeric columns
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Split-apply-combine: group rows by Department, then take mean of Mark per group
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

print("\n--- EDA Summary ---")
print("Highest Mark:", df["Mark"].max())
print("Lowest Mark:", df["Mark"].min())
print("Average Mark:", round(df["Mark"].mean(), 2))
print("Average Attendance:", round(df["Attendance"].mean(), 2))