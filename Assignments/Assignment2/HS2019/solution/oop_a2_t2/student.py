


# -*- coding: utf-8 -*-
"""
oop_a2_t2.student
XX-YYY-ZZZ
<Your name>
"""
from .person import Person

# Define Student class inheriting the Person class
# In addition to the attributes of "Person", "Student" should have
# an "academic_status" attribute and "enroll" method
# The constructor signature: Student(academic_status, name, surname, number)

# Read this article to get more info about exact syntax to inherit from class: https://www.w3schools.com/python/python_inheritance.asp
class Student(Person):
    # I understood the task to do this, references : https://codereview.stackexchange.com/questions/43619/proper-use-of-class-constants; https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
    # Or do we need to create a custom class / struct that contains both variables?
    UNDERGRADUATE="Undergraduate"
    POSTGRADUATE="Postgraduate"
    
    
    def __init__(self, academic_status, name, surname, number, enrolled_courses=list()):
        super().__init__(name, surname, number)
        
        self.academic_status = academic_status
        
        # Empty list is assigned if user does not input a specific list into the constructor
        self.enrolled_courses = enrolled_courses
        
    def enroll_in(self, course):
        # We may have to be aware that the user inputs a course that is already enrolled but has another memory address since the user create a new instance of it with the same name, number etc., that's why we don't only check if the course is in self.enrolled_courses but we check for the name, number etc. in enrolled_courses
        
        # Shorter code, which does not detect when the user inputs different instances of Course with the same attributes:
        #if course not in self.enrolled_courses:
            
        #    self.enrolled_courses.append(course)
        #else:
        #    raise StudentAlreadyEnrolledError
        
        
        # Code that looks if student is already enrolled by looping through course attribute, code (which should be unique) instead of only comparing object instances memory location:
        
        codes=list()
        
        for c in self.enrolled_courses:
            codes.append(c.code)
        
        
        if course.code not in codes:
            self.enrolled_courses.append(course)
        else:
            raise StudentAlreadyEnrolledError
        
        
        
    def summarize(self):
        summarizeString = "Name : {name} {surname}\nStatus : {status}\nCourses : ".format(name = self.name, surname = self.surname, status = self.academic_status)
        for course in self.enrolled_courses:
            summarizeString += "<{}, {}>".format(course.name, course.code)
            
            # Add a comma if there is an additional course afterwards
            if self.enrolled_courses.index(course) < (len(self.enrolled_courses) - 1):
                summarizeString += ", "
            
        
        return summarizeString


# Define StudentAlreadyEnrolledError inheriting Exception class
class StudentAlreadyEnrolledError(Exception):
    """Raised when student is already enrolled in the course"""
    pass
