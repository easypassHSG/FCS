#!/usr/bin/env python3



import numpy

a=[1,3,6,1,2]
b=[3,7,1,10,11]



def maximum_arrays(a,b):
    """This function compares all the elements of two arrays one by one and returns a new array containing the larger elements."""
    
    #First we have to make sure that the arrays have the same length
    if len(a) == len(b):
        
        # We create a new array that can be returned after we added the new elements
        c = []
        
        # I was not sure how the syntax of the for loops are in Python. I found a solution on https://snakify.org/de/lessons/for_loop_range/
        for i in range(0, len(a)):
            
            if a[i] >= b[i]:
                #We call the function insert() and insert the element at the end of c. We get the index of the last position of the array c by len(c). Alternatively, we could have chosen the function append() instead of insert()
                c.insert(len(c), a[i])
            else:
                c.insert(len(c), b[i])
            
            
        return c
    
    else:
        print("Please provide two arrays with the same length")
        


maxArray = maximum_arrays(a,b)
print(maxArray)
