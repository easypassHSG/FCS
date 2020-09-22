#!/usr/bin/env python3


import numpy

a=[1,3,6,1,2]
b=[3,7,1,10,11]


def maximum_arrays(a,b):
    
    #We compare the lengths of the two arrays
    if len(a) == len(b):
        
        #We use the function maximum() that is provided in the numpy module and convert this to a "built-in" list by add the function .tolist()
       return numpy.maximum(a,b).tolist()
    else:
        
        print("Please provide two arrays with the same length")
    
    
    
    
c = maximum_arrays(a, b)
print(c)
