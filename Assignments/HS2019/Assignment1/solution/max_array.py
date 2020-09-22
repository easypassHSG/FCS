#!/usr/bin/env python3


array_a = [1.0, 2.4, 4.0 , 5.1, 1.2]
array_b = [1, 10, 0, -1, 3, 6, 1, 4]


def max_element(array):
    """This function returns the largest value in the array"""
    
    #The function max() returns the highest value of an list
    maxArray = max(array)
    
    
    #Since in our case we want to return the highest number, we will only return a value if the list contains values of type int or float
    if isinstance(maxArray, int) or isinstance(maxArray, float):
        
        return maxArray
    else:
        print("Please provide a list of either Integers or Floating points!")
    
    
    
# We call the function max_element() and print what the function returns
print(max_element(array_a))
print(max_element(array_b))
print(max_element([1.1, 2.2, 3.3, 4.4]))


# We could even create a function that uses the returned value of max_element() and prints some text
def whatIsTheHighestNumberInTheArray(array):
    
    print("The highest number in the array provided is", max_element(array))
    
    
# Let's call the newly created function
whatIsTheHighestNumberInTheArray(array_a)
whatIsTheHighestNumberInTheArray(array_b)
