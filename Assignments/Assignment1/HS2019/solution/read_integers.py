#!/usr/bin/env python3



#We first import the stdio module
import stdio
import sys


def read_file():
    #Then we call the function readAllInts() from the stdio module. As described in the stdio.py file, the function readAllInts() takes the input from the standart input (by calling sys.stdin.readlines()) and groups the integers that were entered into an array (the numbers in the standard input should be delimited with a whitespace).
    return stdio.readAllInts()
    

# Short elaboration:
# We can either pass standard input by running the script in the terminal and then typing characters or by adding < path/to/textFile.txt after the command to run the script. But we can also assign a file to the standard input directly in Thonny by typing the following code (I found that solution with the help of this: https://hplgit.github.io/primer.html/doc/pub/input/._input-readable006.html)

# If you want to input a file directly inside the script uncomment the following line.
# sys.stdin = open('text.txt', 'r')

print(read_file())

#Elaboration on questions in the task:
#If we run the read_integers.py in the terminal we can enter our numbers into the standard input. In the terminal app we signal the end of the standard input by pressing Ctrl+D (Mac) on a new line. We can enter standard input since the function readAllInts() calls the function sys.stdin.readline() which allows us to write something through the standard input.
#If we entered only numbers delimited with spaces we get an array with all the numbers. Otherwise if there is another character, the function readAllInts() throws an error.
#What when we want to not to enter the standard input via the keyboard, but want to read it from a txt file?
#Same as before we call the python script in our terminal by typing: python3 path/read_integers.py. However, this time we add our input file as well. So we type: python3 path/read_integers.py < path/nameOfTextFile.txt. It is important that the text file is plain text (.txt) and not any other format such as .rtf
#Even another way to "assign" a text file to the standard input is as decribed in line 20 (sys.stdin = open('path/to/textFile.txt', 'r'). (This only works if we run the script through Terminal)

