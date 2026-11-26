# Standard convention to import Pandas as pd
import pandas as pd

# 1D labeled array: custom index labels replace default 0..N-1 integer indices
marks = pd.Series([85, 91, 78, 88, 95], index=["A", "B", "C", "D", "E"])
print("--- Pandas Series ---")
print(marks)

# Dict of equal-length lists converts naturally into tabular columns
data = {
    "RollNo": [101, 102, 103, 104, 105],
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE"],
    "Mark": [85, 91, 78, 88, 95],
}

# 2D tabular structure with labeled rows and columns
df = pd.DataFrame(data)
print("\n--- DataFrame ---")
print(df)

# Column selection returns a Series; .mean() computes the arithmetic average
print("\nAverage Mark:", round(df["Mark"].mean(), 2))

# Boolean indexing filters rows where the condition evaluates to True
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])