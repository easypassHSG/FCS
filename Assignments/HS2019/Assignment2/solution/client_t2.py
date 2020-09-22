


# -*- coding: utf-8 -*-
"""A sample client program for oop_a2_t1 and oop_a2_t2 modules"""
from oop_a2_t2 import *
from oop_a2_t1 import Course

def main():
    """ The main function """
    
    # T2.5.1
    
    economics = Course("Economics", "ECO001", 8, 20)
    
    # T2.5.2
    
    nicole = Student(Student.POSTGRADUATE, "Matteo", "Cappellano", 186269)
    
    # Use try statement to handle exception if student is already enrolled
    try:
        
        nicole.enroll_in(economics)
        
                         
    except StudentAlreadyEnrolledError:
        
        # Note that the error is also raised if we assign the same course attributes to two different objects, since the method in Student compares course codes since they should be unique
        print("ERROR: Student is already enrolled in the course.")
        
    
    # I implement a method in Student to return all the necessary information about the student
    print(nicole.summarize())
    
    # Print the type of the object
    print(type(nicole))


    # T2.5.3
    
    if isinstance(nicole, Person):
        print("\nNicole is an instance of the class Person\n")


    # T2.5.4
    
    
    paula = Lecturer(Lecturer.PERMANENT, "Paula", "di Maria", 1002934)
    paula.assign_to(economics)
    
    # To make code more clean we implement a method in Lecturer that returns a summary of the Lecturer
    print(paula.summarize())



    # T2.5.5
    
    if isinstance(paula, Person):
        print("\nPaula is an instance of the class Person\n")
    if isinstance(paula, StaffMember):
        print("\nPaula is an instance of the class StaffMember\n")





if __name__ == "__main__":
    main()
