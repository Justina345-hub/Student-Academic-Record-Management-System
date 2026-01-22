# -------------------------------------------------
# Student Academic Record Management System
# Student: Justina Mwango
# -------------------------------------------------
# This program helps manage student academic records
# using dictionaries only.
#
# I focused on:
# - clear logic
# - correct calculations
# - readable structure
# - small validations to avoid errors
# -------------------------------------------------

students = {}   # main dictionary to store all student records


#ADD STUDENT
def add_student():
    print("\n--- Add New Student ---")

    student_id = input("Enter Student ID: ")

    # prevent duplicate IDs
    if student_id in students:
        print("This Student ID already exists. Please try again.")
        return

    name = input("Enter Full Name: ")
    class_name = input("Enter Class: ")

    subjects = {}

    # at least 3 subjects are required
    for i in range(3):
        subject = input(f"Enter subject {i + 1} name: ")
        mark = int(input(f"Enter mark for {subject}: "))

        # mark validation
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return

        subjects[subject] = mark

    # storing all student details
    students[student_id] = {
        "name": name,
        "class": class_name,
        "subjects": subjects
    }

    print("You Have Successfully Added a New Student🌟")


#VIEW ALL STUDENTS
def view_all_students():
    print("\n--- All Registered Students ---")

    if not students:
        print("No students found yet.")
        return

    for student_id, details in students.items():
        print(f"ID: {student_id} | Name: {details['name']}")


#CALCULATE AVERAGE
def calculate_average(subjects):
    total = sum(subjects.values())
    return total / len(subjects)


#CALCULATE GRADE
def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


#STUDENT REPORT
def view_student_report():
    print("\n--- Student Academic Report ---")

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    subjects = student["subjects"]

    total = sum(subjects.values())
    average = calculate_average(subjects)
    grade = calculate_grade(average)

    print("\nName:", student["name"])
    print("Class:", student["class"])

    print("\nSubjects and Marks:")
    for subject, mark in subjects.items():
        print(f"{subject}: {mark}")

    print("\nTotal Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)


#UPDATE MARKS
def update_marks():
    print("\n--- Update Student Marks ---")

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name to update: ")

    if subject not in students[student_id]["subjects"]:
        print("Subject not found.")
        return

    new_mark = int(input("Enter new mark: "))

    if new_mark < 0 or new_mark > 100:
        print("Invalid mark entered.")
        return

    students[student_id]["subjects"][subject] = new_mark
    print("Marks updated successfully ✔️")


#DELETE STUDENT
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        del students[student_id]
        print("Student record deleted.")
    else:
        print("Student not found.")


#BONUS: RANK STUDENTS 
def rank_students():
    print("\n--- Student Rankings ---")

    if not students:
        print("No students available to rank.")
        return

    averages = {}

    for student_id, details in students.items():
        averages[student_id] = calculate_average(details["subjects"])

    ranked = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    position = 1
    for student_id, avg in ranked:
        print(f"{position}. {students[student_id]['name']} - Average: {round(avg, 2)}")
        position += 1


#BONUS: TOP STUDENT 
def top_student():
    print("\n--- Top Performing Student ---")

    if not students:
        print("No student records available.")
        return

    best_id = None
    best_avg = 0

    for student_id, details in students.items():
        avg = calculate_average(details["subjects"])
        if avg > best_avg:
            best_avg = avg
            best_id = student_id

    print("Name:", students[best_id]["name"])
    print("Class:", students[best_id]["class"])
    print("Average:", round(best_avg, 2))
    print("Grade:", calculate_grade(best_avg))


# BONUS: SUBJECT AVERAGES
def subject_averages():
    print("\n--- Subject-wise Averages ---")

    if not students:
        print("No data available.")
        return

    subject_totals = {}
    subject_counts = {}

    for details in students.values():
        for subject, mark in details["subjects"].items():
            subject_totals[subject] = subject_totals.get(subject, 0) + mark
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    for subject in subject_totals:
        average = subject_totals[subject] / subject_counts[subject]
        print(f"{subject}: {round(average, 2)}")


# MAIN MENU 
def menu():
    while True:
        print(" Student Academic Record System ")
        print("************************************")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Report")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Rank Students ")
        print("7. Top Performing Student ")
        print("8. Subject-wise Averages")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            view_student_report()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            rank_students()
        elif choice == "7":
            top_student()
        elif choice == "8":
            subject_averages()
        elif choice == "9":
            print("\nThank you for using the system 🌱")
            print("Keep learning and improving. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# program starts here
menu()
