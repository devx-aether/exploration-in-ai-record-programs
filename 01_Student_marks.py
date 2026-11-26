# Read text input from standard input (returns a string)
name = input("Enter student name: ")

# Convert the string input to an integer for loop bounds and division
n = int(input("Enter number of subjects: "))

# Accumulator variable to sum marks across all subjects
total = 0

# range(1, n + 1) generates 1, 2, ..., n so subject numbering starts at 1
for i in range(1, n + 1):
    # Use float so fractional/decimal marks are preserved instead of truncating or crashing
    mark = float(input(f"Enter mark for Subject {i}: "))
    total += mark

# Average mark across n subjects (assuming each subject is out of 100)
percentage = total / n

# Evaluate from highest threshold downward so only the first matching branch runs
if percentage >= 90:
    grade = "A+"
    performance = "Outstanding"
elif percentage >= 80:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage >= 60:
    grade = "C"
    performance = "Good"
elif percentage >= 50:
    grade = "D"
    performance = "Average"
else:
    grade = "F"
    performance = "Needs Improvement"

print("\n--- Academic Performance ---")
print("Student Name:", name)
print("Total Marks:", total)
# round(value, 2) limits displayed decimals to 2 places without altering `percentage`
print("Percentage:", round(percentage, 2), "%")
print("Grade       :", grade)
print("Performance:", performance)