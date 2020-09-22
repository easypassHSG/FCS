


# -*- coding: utf-8 -*-
"""
oop_a2_t1.course
XX-YYY-ZZZ
<Your name>
"""
from .student import Student

class Course:
    def __init__(self, name, code, credit, student_limit, students=list()):
        # Your code for the constructor
        
        self.name = name
        self.code = code
        self.credit = credit
        self.student_limit = student_limit
        
        self.students = students
        

    def add_student(self, student):
        # Your code to add a student to the course
        if len(self.students) < self.student_limit:
            self.students.append(student)
        else:
            raise CourseCapacityFullError
        

    def remove_student_by_number(self, student_number):
        # Your code to remove a student by the number from the course
        numbers = list()
        
        
        for student in self.students:
            numbers.append(student.number)
        
        try:
            # pop() removes element at certain index, found on: https://thispointer.com/python-how-to-remove-element-from-a-list-by-value-or-index-remove-vs-pop-vs-del/
            
            self.students.pop(numbers.index(student_number))
        except:
            raise StudentNotEnrolledError
            
            
        
        
        

    def to_string(self):
        # Your code to return a string containing:
        # - the course name
        # - the course code
        # - the maximum number of students
        # - the number of students enrolled
        # - the list of enrolled students
        
        # I read about .format() to add variables to string on : https://pyformat.info 
        string_to_return = "===Course information===\nName : {course_name}\nCode : {course_code}\nMaximum students : {max_students}\nNumber of Students enrolled : {number_enrolled_students}\nEnrolled students :".format(course_name=self.name, course_code=self.code, max_students=str(self.student_limit), number_enrolled_students=str(len(self.students)))
        
        for student in self.students:
            string_to_return += "\n- {student_name} <{student_number}>".format(student_name=student.name, student_number=student.number)
            
        
        return string_to_return

class CourseCapacityFullError(Exception):
    """Raised when adding a student to the course and it is already full"""
    pass

class StudentNotEnrolledError(Exception):
    """Raised when removing a student from the course and the student is not enrolled"""
    pass
