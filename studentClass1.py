# setting up the student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # method to return student grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # Empty list

    def add_student(self, student):
        # Test that there is room in the course
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    # method to get average grade
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)


# Instantiate 3 student objects
s1 = Student(name="Tim", age=19, grade=95)
s2 = Student(name="Bill", age=19, grade=75)
s3 = Student(name="Jill", age=19, grade=65)

# print(Student.get_grade(s1))
# print(Student.get_grade(s2))
# print(Student.get_grade(s3))

# instantiate course subject
course1 = Course(name="Computer Science", max_students=3)

course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)

# confirm entry of students
for student in course1.students:
    print(f"{student.name} aged {student.age} got a grade of {student.grade}")

# get the average grade of all students
print(f"The average grade in {course1.name} is {course1.get_average_grade().__round__(2)} ")
