# setting up the student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # method to return student grade
    def get_grade(self):
        return self.grade

    # Instantiate student objects
