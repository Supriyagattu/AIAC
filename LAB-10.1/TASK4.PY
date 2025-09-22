students = ["Alice", "Bob", "Charlie"]

def welcome_student(student):
    """Print a welcome message for a single student.

    Args:
        student (str): The name of the student to welcome.
    """
    print("Welcome", student)

def welcome_all_students(student_list):
    """Welcome each student in the provided list.

    Args:
        student_list (list of str): List of student names.
    """
    for student in student_list:
        welcome_student(student)

welcome_all_students(students)






