# Dictionary mapping roll number (key) -> dict of student details (value)
students = {}


def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    # Overwrites existing entry if `roll` is already present
    students[roll] = {"Name": name, "Department": dept}
    print("Student added successfully.")


def view_students():
    # Empty dict evaluates to False in boolean context
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    # .items() yields (key, value) pairs for iteration
    for roll, data in students.items():
        print(
            "Roll No:",
            roll,
            "| Name:",
            data["Name"],
            "| Department:",
            data["Department"],
        )


def search_student():
    roll = input("Enter Roll No to search: ")
    # `in` checks dictionary keys in O(1) average time
    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        # `del` removes the key-value pair in-place
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


# Keep menu running until the user explicitly chooses Exit (option 5)
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    # input() returns a str, so compare against string literals "1".."5"
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")