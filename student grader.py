students = {}

def show_menu():
    print("\n=== STUDENT GRADE TRACKER ===")
    print("1. Add Student Grade")
    print("2. View All Grades")
    print("3. Edit Student Grade")
    print("4. Remove Student")
    print("5. Calculate Average Grade")
    print("6. Exit")

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students[name] = grade
    print("Student added successfully.")

def view_grades():
    if not students:
        print("\nNo student records found.")
    else:
        print("\n--- Student Grades ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")

def edit_grade():
    name = input("Enter student name to edit: ")
    if name in students:
        new_grade = float(input("Enter the new grade: "))
        students[name] = new_grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        del students[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")

def average_grade():
    if not students:
        print("No grades to calculate average.")
    else:
        avg = sum(students.values()) / len(students)
        print(f"Class Average Grade: {avg:.2f}")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_grades()
    elif choice == "3":
        edit_grade()
    elif choice == "4":
        remove_student()
    elif choice == "5":
        average_grade()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")