



# -*- coding: utf-8 -*-
"""
oop_a2_t2.lecturer
XX-YYY-ZZZ
<Your name>
"""
from .staff_member import StaffMember

# Define Lecturer class inheriting the StaffMember class
# In addition to the attributes of "StaffMember", "Lecturer" should have
# a list attribute "taught_courses"

class Lecturer(StaffMember):
    
    
    def __init__(self, employment_type, name, surname, number, assigned_courses=list()):
        
        super().__init__(employment_type, name, surname, number)
        
        
        self.assigned_courses = assigned_courses
    
    
    def assign_to(self, course):
        
        self.assigned_courses.append(course)
        
        
        
        
    def summarize(self):
        
        stringReturn = "\nName : {name} {surname}\nEmployment type : {status}\nCourses : ".format(name = self.name, surname = self.surname, status = self.employment_type)
        
        for course in self.assigned_courses:
            stringReturn += "<{}, {}>".format(course.name, course.code)
            
            # Add a comma if there is an additional course afterwards
            if self.assigned_courses.index(course) < (len(self.assigned_courses) - 1):
                stringReturn += ", "
            
        
        
        return stringReturn