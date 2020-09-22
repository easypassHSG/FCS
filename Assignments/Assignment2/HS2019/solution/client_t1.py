"""A sample client program for oop_a2_t1 module"""
from oop_a2_t1 import *

def main():
    """ The main function """
    # Create a new Department class instance
    math_dept = Department("Mathematics and Applied Mathematics", "MAM")
    # Create a new Course class instance
    math_course = Course("Mathematics 1000", "MAM1000W", 1, 10)
    # Add the math course to the math dept
    
    math_dept.add_course(math_course)
    # Create a new Student class instance Alice
    alice = Student("Alice", 1336)
    # Create another new Student class instance Bob
    bob = Student("Bob", 1337)

    # Add Alice to the math course
    math_course.add_student(alice)

    # Add Bob to the math course
    math_course.add_student(bob)

    # Remove Alice from the math course
    math_course.remove_student_by_number(alice.number)
    

    # Try remove Alice from the math course again
    try:
        math_course.remove_student_by_number(alice.number)
    except StudentNotEnrolledError:
        print("ERROR: Student %s not enrolled in %s" % (alice.name, math_course.name))

    # Try adding 10 more students
    for i in range(10):
        try:
            math_course.add_student(Student("Student_"+str(i), 1338+i))
        except CourseCapacityFullError:
            print("ERROR: %s is already full" % math_course.name)

    # Print the course
    print(math_course.to_string())

if __name__ == "__main__":
    main()
