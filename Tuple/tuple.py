def main():
    # Sample list of student records stored as tuples
    students = [
        
    ]

    # Main menu loop
    while True:
        print("\nStudent Records Management")
        print("1. View all student records")
        print("2. Add a new student record")
        print("3. Update a student's scores")
        print("4. Delete a student record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_students(students)
        elif choice == "2":
            students = add_student(students)
        elif choice == "3":
            students = update_scores(students)
        elif choice == "4":
            students = delete_student(students)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def calculate_final_grade(scores):
    """Calculate final grade as the average of scores."""
    return sum(scores) / len(scores)


def view_students(students):
    """Display all student records."""
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records:")
    for student in students:
        name, scores = student
        final_grade = calculate_final_grade(scores)
        print(f"Name: {name}, Scores: {scores}, Final Grade: {final_grade:.2f}")


def add_student(students):
    """Add a new student record."""
    name = input("Enter the student's name: ")
    scores = input("Enter the student's exam scores (comma-separated): ")
    scores = list(map(int, scores.split(",")))

    students.append((name, scores))
    print(f"Student {name} added successfully.")
    return students


def update_scores(students):
    """Update a student's scores."""
    name = input("Enter the student's name to update scores: ")

    for i, student in enumerate(students):
        if student[0] == name:
            new_scores = input("Enter the new scores (comma-separated): ")
            new_scores = list(map(int, new_scores.split(",")))
            students[i] = (name, new_scores)
            print(f"Scores for {name} updated successfully.")
            return students

    print(f"Student {name} not found.")
    return students


def delete_student(students):
    """Delete a student record."""
    name = input("Enter the student's name to delete: ")

    for i, student in enumerate(students):
        if student[0] == name:
            students.pop(i)
            print(f"Student {name} deleted successfully.")
            return students

    print(f"Student {name} not found.")
    return students


if __name__ == "__main__":
    main()
