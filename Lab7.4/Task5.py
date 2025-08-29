class CourseRecord:
    def __init__(self, course_name, course_code, instructor):
        self.name = course_name
        self.code = course_code
        self.teacher = instructor

    def get_info(self):
        return f"{self.name} ({self.code}) - Taught by {self.teacher}"


class Student:
    def __init__(self, name, student_id, enrolled_courses=None):
        self.full_name = name
        self.id = student_id
        self.courses = enrolled_courses if enrolled_courses is not None else []

    def enroll(self, course):
        self.courses.append(course)

    def get_summary(self):
        course_names = ', '.join([c.name for c in self.courses])
        return f"Student: {self.full_name}, ID: {self.id}, Enrolled: {course_names}"


class University:
    def __init__(self, univ_name, student_list=None):
        self.university = univ_name
        self.students = student_list if student_list is not None else []

    def register(self, student):
        self.students.append(student)

    def get_overview(self):
        return f"{self.university} has {len(self.students)} students enrolled."


# ---------- Testing the Classes Below ----------

# Create course instances
c1 = CourseRecord("Computer Science", "CS101", "Dr. Smith")
c2 = CourseRecord("Mathematics", "MATH101", "Dr. Jones")

# Create student and enroll in courses
s1 = Student("Alice", 1001)
s1.enroll(c1)
s1.enroll(c2)

# Create university and register the student
uni = University("Tech University")
uni.register(s1)

# Output summaries
print(s1.get_summary())
print(uni.get_overview())
