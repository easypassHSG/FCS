# -*- coding: utf-8 -*-
"""
sorter.py
<Your Name>
<Your ID>
"""
from sys import maxsize
from time import time
### Other imports for your tasks ###

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



        ### Task 4 END ###
        return lst


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



        ### Task 3 END ###
        return lst


    def _merge_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with Merge Sort algorithm.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The merge_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        lst = list(self.unsorted_tuple)
        ###   Task 5   ###



        ### Task 5 END ###
        return lst


class AlgorithmNotImplementedError(Exception):
    """Raised when an nknown algorithm was selected"""
    pass
