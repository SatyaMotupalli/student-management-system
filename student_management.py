import os
import json

# Define the student database file
DB_FILE = "students.json"

# Load existing data or create new
def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(students):
    with open(DB_FILE, "w") as f:
        json.dump(students, f, indent=4)

# Add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    student = {"roll": roll, "name": name, "branch": branch}

    students = load_data()
    students.append(student)
    save_data(students)
    print("✅ Student added successfully!")

# View all students
def view_students():
    students = load_data()
    if not students:
        print("⚠️ No students found.")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Branch: {s['branch']}")

# Search student
def search_student():
    roll = input("Enter Roll Number to search: ")
    students = load_data()
    for s in students:
        if s["roll"] == roll:
            print(f"🎯 Found: Name: {s['name']}, Branch: {s['branch']}")
            return
    print("❌ Student not found.")

# Update student
def update_student():
    roll = input("Enter Roll Number to update: ")
    students = load_data()
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["branch"] = input("Enter new branch: ")
            save_data(students)
            print("✅ Student updated.")
            return
    print("❌ Student not found.")

# Delete student
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    students = load_data()
    new_students = [s for s in students if s["roll"] != roll]
    if len(new_students) == len(students):
        print("❌ Student not found.")
    else:
        save_data(new_students)
        print("🗑️ Student deleted.")

# Menu
def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

# Run the program
menu()
