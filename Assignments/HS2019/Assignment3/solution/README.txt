

*Task 2*

a) Why have some methods underscores (“_”) and some not?
-	Underscores in classes are used to signal that a method is private, which means it should only be accessed and called from inside (internal) the class and not from outside (more concretely, e.g. the method _default_sort() should only be called from the e.g. the time_trials() method (so from inside the class) but not from outside. However, the single underscore is only used as a “hint” to the programmer but doesn’t prevent us from accessing the fuction from outside (e.g. in the doubling_test.py file we could still access the function like this sorter._default_sort() ). So, it is just a convention, which is also defined by PEP 8. Also, can the underscore be used at the beginning of the name of a class constant in order to signal a private class attribute. (However, when importing all modules from a package the single underscore can make a difference: if we call e.g. from x import * python will only import all methods that are public)


b)
a tuple and a list basically are very similar. However, the main difference is that tuples are immutable (cannot be changed) while list can be changed. In our case having a immutable tuple can be useful so that we know that we can only change something if we firstly create a copy of the tuple and convert it to a list. This is especially useful since in Python we can only make a copy of a list when appending .copy(), otherwise the same object is just assigned to another variable name – in order to be sure that we don’t change the variable self.unsorted_tuple, using the type tuple is useful.


c)

time() returns the time (seconds) that passed since the epoch in a floating point number. As written in the documentation, "the epoch is the point where the time starts, and is platform dependent". This means on a Max (Unix) the function returns the seconds passed since January 1, 1970, 00:00:00 (UTC).
This return value is for example used in the time_trials() method, where a starttime is set (numbers of seconds passed since 1970). Afterwards, before returning we can use this starttime and subtract it from the exact time right then.. which gives us the time difference (the time the function needed to execute in seconds).


d)


n:
So, n is an input of the function argument and defines how many times the for loop is executed. This means it tells us how many times the sorting of the array is performed (so, range(n) will iterate from 0 to n times through the loop) until the function returns the time it took to run the code.


algorithm:
self.algorithm is a class attribute of Sorter, which we can define with the method set_algorithm() and which is set to "default" in the initializer of the class. In set_algorithm() we can see that the attribute self.algorithm can only take a limited number of possible values, namely 'default', 'merge', 'insertion', 'bubble'. So, in the function time_trials() we can use these values to define which sorting algorithm (i.e. which method should be called). For example, if self.algorithm is equal to 'merge' we will call the method _merge_sort() since we there have defined the function that performs a merge sort.

is_reverse:
Normally reverse is set to False, so the list will be sorted in ascending order. However, in all the methods for sorting we have an argument that can specify if we want to sort in descending order – this can be done by inputing reverse=True as a function argument. We can see that is_reverse (which then is inputed as argument into the sorting method) is always changed. More precisely, if we loop through the for loop for the first time i will be equal to 0 and i%2 == 0 will be True, this means in the first iteration we will sort in descending order, however in the second iteration i will be 1 and i%2==0 will be False.. this means in the second iteration we will sort in ascending order. This change is useful to make sure that the algorithm isn't only fast to sort in either descending or ascending order but for both ways.




*Task 6:*

Observations for the different algorithms:

Bubble sort:

n:      64 time: 0.062070 (n:n/2) ratio: -
n:     128 time: 0.226325 (n:n/2) ratio: 3.646279
n:     256 time: 0.876278 (n:n/2) ratio: 3.871768
n:     512 time: 3.678104 (n:n/2) ratio: 4.197417
n:    1024 time: 15.563879 (n:n/2) ratio: 4.231495
n:    2048 time: 63.659193 (n:n/2) ratio: 4.090188
n:    4096 time: 275.361420 (n:n/2) ratio: 4.325556


Insertion sort:

n:      64 time: 0.042508 (n:n/2) ratio: -
n:     128 time: 0.156579 (n:n/2) ratio: 3.683502
n:     256 time: 0.624200 (n:n/2) ratio: 3.986491
n:     512 time: 2.725985 (n:n/2) ratio: 4.367167
n:    1024 time: 11.569229 (n:n/2) ratio: 4.244055
n:    2048 time: 47.440906 (n:n/2) ratio: 4.100611
n:    4096 time: 205.155104 (n:n/2) ratio: 4.324435



Merge sort:

n:      64 time: 0.021926 (n:n/2) ratio: -
n:     128 time: 0.048207 (n:n/2) ratio: 2.198619
n:     256 time: 0.099635 (n:n/2) ratio: 2.066806
n:     512 time: 0.226144 (n:n/2) ratio: 2.269722
n:    1024 time: 0.469786 (n:n/2) ratio: 2.077376
n:    2048 time: 1.017376 (n:n/2) ratio: 2.165615
n:    4096 time: 2.242661 (n:n/2) ratio: 2.204358



Doubling hypotheses:
With each increase of the input size by two the algorithm will take X time longer (order of growth). For example, a algorithm can have an order of growth which is quadratic, this means that with each increasal of the input size (n) by two the time it takes will be fourfold (on a log to log scale this would correspond to a slope of 2).

For both the insertion and bubble sort we can see that for each doubling of the input size (n) the time it takes is fourfold (so the factor for doubling hypothesis is 4). This means that the order of growth of the two algorithms is quadratic O(n^2). Which completely makes sense when we know the implementation of the two algorithms (both have a loop inside a loop).

For the merge sort we can see that it is much more efficient. Each doubling of the input size only results in a time increase of around 2 (so it has factor for doubling hypotheses of 2), which is much faster in the case of high input sizes (n). Merge sort has a linearithmic order of growth, O(n * log(n))