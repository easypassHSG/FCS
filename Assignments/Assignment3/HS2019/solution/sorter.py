# -*- coding: utf-8 -*-
"""
sorter.py
<Your Name>
<Your ID>
"""
from sys import maxsize
from time import time

### Other imports for your tasks ###
import random
import sys

####################################


class Sorter():
    """Sorter implements several algorithms to sort a list.

    `unsorted_tuple`: A tuple of random integers to be sorted.

    `algorithm`: A string contains name of the algorithm to be used for sorting.
                 Valid valus are 'bubble', 'default', 'insert', and 'merge'.

    Each sorting method make a list copy of `unsorted_tuple` and maintains the original order.

    """

    def __init__(self):
        """Sorter constructor.

        By default, the `algorithm` is set as 'default' to use the built-in sort()

        """
        self.unsorted_tuple = tuple([])
        self.algorithm = 'default'
           
        
        
        


    def generate_new_tuple(self, n):
        """Generate a n-length tuple of random integers for `unsorted_tuple`

        `n` is an integer indicates the length of the list.

        Random integers are in a range from 0 to 9223372036854775807 (sys.maxsize)

        The method generate_new_tuple() first generates a new list of `n` length
        containing random integers, converts the newly generated list to a tuple,
        assigns the tuple to `self.unsorted_tuple`, and returns None.

        """
        ###   Task 1(a)   ###
        
        list_ = list()
        
        for _ in range(n):
            list_.append(random.randint(0,sys.maxsize))
            
            
        tuple_ = tuple(list_)
        self.unsorted_tuple = tuple_
        
        
        return None

        ### Task 1(a) END ###


    def set_algorithm(self, algo):
        """Set the attribute to select which algorithm to be used for sort()."""
        # Check if the given algorithm is valid
        if algo not in ['default', 'merge', 'insertion', 'bubble']:
            raise AlgorithmNotImplementedError
        self.algorithm = algo


    def time_trials(self, n):
        """Time sorting `self.unsorted_tuple` with a specific algorithm for n times.

        `n` is an integer value. The sorting will be performed `n` times.

        The method time_trials() returns a float value for how long it took in seconds.

        """
        start_time = time() # current time

        for i in range(n):
            is_reverse = (i%2 == 0)
            if self.algorithm == 'merge':
                self._merge_sort(is_reverse)
            elif self.algorithm == 'insertion':
                self._insertion_sort(is_reverse)
            elif self.algorithm == 'bubble':
                self._bubble_sort(is_reverse)
            else:
                self._default_sort(is_reverse)

        return time() - start_time # time elapsed


    def _bubble_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with Bubble Sort algorithm.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The bubble_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        lst = list(self.unsorted_tuple)
        ###   Task 4   ###
        
        
        def _sortingOrderComparison(reverse, i):
            """Depening on the fact if we should sort in descending or ascending order the function return either True or False which can be used in another if statement"""
            
            if reverse == True:
                if lst[i] < lst[i + 1]:
                    return True
                else:
                    return False
            else:
                if lst[i] > lst[i + 1]:
                    return True
                else:
                    return False
        
        n = len(lst) - 1
        
        
        while n > 0:
            for i in range(0, n):
                
                if _sortingOrderComparison(reverse, i):
                    firstElement = lst[i]
                    secondElement = lst[i + 1]
                    
                    lst[i] = secondElement
                    lst[i + 1] = firstElement
                     
            # we can subtract 1 from n since we know that the last element is the highest number in the whole list, so we don't need to check if anymore
            n -= 1
            
            
        ### Task 4 END ###
        return list(lst)


    def _default_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with the Python built-in list sorting function.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The default_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        # Make a list copy of self.unsorted_tuple
        lst = list(self.unsorted_tuple)
        # sort the list by the Python built-in list.sort()
        # https://docs.python.org/3/library/stdtypes.html#list.sort
        lst.sort(reverse=reverse)
        return lst


    def _insertion_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with Insertion Sort algorithm.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The insertion_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        lst = list(self.unsorted_tuple)
        ###   Task 3   ###
        
        def _sortingOrderComparison(reverse):
            """ Returns either True or False depending on reverse, the returns a bool that can be used."""
            if reverse == True:
                if lst[j] > lst[j - 1]:
                    return True
                else:
                    return False
            else:
                if lst[j] < lst[j - 1]:
                    return True
                else:
                    return False
                
        
        n = len(lst)
        
        for i in range(1, n):
            j = i
            
            while _sortingOrderComparison(reverse) and (j > 0):
                
                # Exchange the elements
                firstElement = lst[j]
                secondElement = lst[j - 1]
                
                lst[j] = secondElement
                lst[j - 1] = firstElement
                
                j -= 1
            
        ### Task 3 END ###
        
        return list(lst)


    def _merge_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with Merge Sort algorithm.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The merge_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        lst = list(self.unsorted_tuple)
        ###   Task 5   ###
        
        def _mergeSort(list_, lengthList):
            if len(list_) > 1:
                
                mid = len(list_)//2
                leftSide = list_[:mid]
                rightSide = list_[mid:]
                
                _mergeSort(leftSide, lengthList)
                _mergeSort(rightSide, lengthList)
                
                i = 0 #LeftSide counter
                j = 0 #RightSide counter
                k = 0 #list_ index counter
                
                while i < len(leftSide) and j < len(rightSide):
                    if leftSide[i] < rightSide[j]:
                        
                        if reverse == False:
                            list_[k] = leftSide[i]
                            i += 1
                        else:
                            list_[k] = rightSide[j]
                            j += 1
                        
                    else:
                        if reverse == False:
                            list_[k] = rightSide[j]
                            j += 1
                        else:
                            list_[k] = leftSide[i]
                            i += 1
                        
                    k += 1
                
                while i < len(leftSide):
                    list_[k] = leftSide[i]
                    i += 1
                    k += 1
                    
                while j < len(rightSide):
                    list_[k] = rightSide[j]
                    j += 1
                    k += 1
                    
                if len(list_) >= lengthList:
                    
                    return list_
            
                
        
        
        lst = _mergeSort(lst, len(lst))
        

        ### Task 5 END ###
        return list(lst)


class AlgorithmNotImplementedError(Exception):
    """Raised when an nknown algorithm was selected"""
    pass
