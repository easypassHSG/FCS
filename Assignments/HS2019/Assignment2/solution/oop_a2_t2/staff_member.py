


# -*- coding: utf-8 -*-
"""
oop_a2_t2.staff_member
XX-YYY-ZZZ
<Your name>
"""
from .person import Person

# Define StaffMember class inheriting the Person class
# In addition to the attributes of "Person", "StaffMember" should have
# an "employment_type" attribute
# The constructor signature: StaffMember(employment_type, name, surname, number)


class StaffMember(Person):
    
    TEMPORARY="Temporary"
    PERMANENT="Permanent"
    
    
    def __init__(self, employment_type, name, surname, number):
        
        super().__init__(name, surname, number)
        
        self.employment_type = employment_type
        
