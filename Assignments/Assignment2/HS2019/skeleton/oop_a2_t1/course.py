# -*- coding: utf-8 -*-
"""
oop_a2_t1.course
XX-YYY-ZZZ
<Your name>
"""
from .student import Student

class Course:
    def __init__(self, name, code, credit, student_limit):
        # Your code for the constructor

    def add_student(self, student):
        # Your code to add a student to the course

    def remove_student_by_number(self, student_number):
        # Your code to remove a student by the number from the course

    def to_string(self)
        # Your code to return a string containing:
        # - the course name
        # - the course code
        # - the maximum number of students
        # - the number of students enrolled
        # - the list of enrolled students

class CourseCapacityFullError(Exception):
    """Raised when adding a student to the course and it is already full"""
    pass

class StudentNotEnrolledError(Exception):
    """Raised when removing a student from the course and the student is not enrolled"""
    pass
