print("📚 Student Management System (PRO VERSION)")

students = []

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    # ADD STUDENT
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")

        # NEW FEATURE: marks
        try:
            marks = float(input("Enter marks (out of 100): "))
        except:
            print("❌ Invalid marks, set to 0")
            marks = 0

        student = {
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)
        print("✅ Student added successfully!")

    # VIEW STUDENTS
    elif choice == "2":
        if len(students) == 0:
            print("No students found ❌")
        else:
            print("\nName | Age | Marks")
            print("---------------------")
            for s in students:
                print(s["name"], "|", s["age"], "|", s["marks"])

    # SEARCH
    elif choice == "3":
        search = input("Enter name: ")
        found = False

        for s in students:
            if s["name"].lower() == search.lower():
                print("Found →", s["name"], "| Age:", s["age"], "| Marks:", s["marks"])
                found = True
                break

        if not found:
            print("Student not found ❌")

    # DELETE
    elif choice == "4":
        name = input("Enter name to delete: ")
        removed = False

        for s in students:
            if s["name"].lower() == name.lower():
                students.remove(s)
                print("Deleted successfully 🗑️")
                removed = True
                break

        if not removed:
            print("Student not found ❌")

    # EXIT
    elif choice == "5":
        print("Exiting... Bye 👋")
        break

    else:
        print("Invalid choice ❌")