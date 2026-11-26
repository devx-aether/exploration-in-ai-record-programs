# Built-in module for reading and writing comma-separated values files
import csv

# List of dictionaries: each element is one student record with named fields
students = [
    {"RollNo": "101", "Name": "Anitha", "Department": "CSE", "Mark": 86},
    {"RollNo": "102", "Name": "Bala", "Department": "CSE", "Mark": 91},
    {"RollNo": "103", "Name": "Chitra", "Department": "ECE", "Mark": 78},
]

# Tuple is immutable: useful for fixed metadata like course name and credits
course = ("Python", 4)
print("Course Tuple:", course)

# `with` context manager automatically closes the file block when done
with open("students.txt", "w") as file:
    for student in students:
        # Convert dict to its string representation and append a newline
        file.write(str(student) + "\n")

# newline="" prevents extra blank lines on Windows when writing CSVs
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]
    # DictWriter maps dictionary keys to CSV columns using `fieldnames`
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

print("\n--- Records from CSV ---")
with open("students.csv", "r") as file:
    # DictReader uses the header row as keys for each subsequent row dict
    reader = csv.DictReader(file)
    for row in reader:
        print(row["RollNo"], row["Name"], row["Department"], row["Mark"])