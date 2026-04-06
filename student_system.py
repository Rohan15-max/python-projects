print("📚 Student Management System")

students = []

while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")

        student = {
            "name": name,
            "age": age
        }

        students.append(student)
        print("✅ Student added successfully!")

    # View students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for i, s in enumerate(students):
                print(i+1, s["name"], "-", s["age"])

    # Search student
    elif choice == "3":
        search = input("Enter name to search: ")
        found = False

        for s in students:
            if s["name"].lower() == search.lower():
                print("Found:", s["name"], "-", s["age"])
                found = True
                break

        if not found:
            print("Student not found ❌")

    # Delete student
    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        removed = False

        for s in students:
            if s["name"].lower() == delete_name.lower():
                students.remove(s)
                print("Deleted successfully 🗑️")
                removed = True
                break

        if not removed:
            print("Student not found ❌")

    # Exit
    elif choice == "5":
        print("Exiting system... Bye 👋")
        break

    else:
        print("Invalid choice ❌")