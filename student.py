import re

# List to store student dictionaries
students = []

FILE_NAME = "students.txt"


# Validate email using Regex
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


# Save the entire list to the file
def save_to_file():
    try:
        with open(FILE_NAME, "w") as file:
            for student in students:
                file.write(str(student) + "\n")

    except Exception as e:
        print("Error while saving file:", e)


# Read student data from file
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
            else:
                print("\n--- Student Records ---")

                for line in data:
                    print(line.strip())

    except FileNotFoundError:
        print("students.txt file not found.")


# Add a student
def add_student():
    try:
        roll_no = input("Enter Roll No: ").strip()
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        course = input("Enter Course: ").strip()

        # Check for empty input
        if not roll_no or not name or not email or not course:
            raise ValueError("All fields are required.")

        # Validate email
        if not validate_email(email):
            raise ValueError("Invalid email format.")

        # Create student dictionary
        student = {
            "Roll No": roll_no,
            "Name": name,
            "Email": email,
            "Course": course
        }

        # Add dictionary to list
        students.append(student)

        # Save updated list to file
        save_to_file()

        print("Student details saved in students.txt")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


# Search student by Roll No
def search_student():
    try:
        roll_no = input("Enter Roll No to search: ").strip()

        if not roll_no:
            raise ValueError("Roll No cannot be empty.")

        found = False

        # Search through the list
        for student in students:
            if student["Roll No"] == roll_no:
                print("\nStudent Found:")
                print("Roll No:", student["Roll No"])
                print("Name:", student["Name"])
                print("Email:", student["Email"])
                print("Course:", student["Course"])

                found = True
                break

        if not found:
            print("Student not found")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


# Main menu
def main():
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                search_student()

            elif choice == "4":
                print("Program exited.")
                break

            else:
                raise ValueError("Invalid menu choice. Please enter 1-4.")

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Error:", e)


# Start the program
if __name__ == "__main__":
    main()
