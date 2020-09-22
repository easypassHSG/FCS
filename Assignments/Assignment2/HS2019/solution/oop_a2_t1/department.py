

# -*- coding: utf-8 -*-
"""
oop_a2_t1.department
XX-YYY-ZZZ
<Your name>
"""
from .course import Course

class Department:
    def __init__(self, name, code, courses=list()):
        # Your code for the constructor
        self.name = name
        self.code = code
        
        #We could also define an empty list for courses, however if we want we can already input a list of courses in the constructor (optional)
        self.courses = courses
        
        
        
        

    def add_course(self, course):
        # Your code to add the `course` to this instance's `courses`
        
        # We only take inputs of type Course, otherwise we inform the user.
        if isinstance(course, Course):
            self.courses.append(course)
        else:
            print("Please provide an argument of type oop_a2_t1.course.Course – not", type(course) ,"– into the method Department.add_course().")
