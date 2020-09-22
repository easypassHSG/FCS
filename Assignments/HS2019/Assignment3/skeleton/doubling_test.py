# -*- coding: utf-8 -*-
"""

!!! PLEASE DO NOT CHANGE THIS FILE !!!

"""

from sorter import AlgorithmNotImplementedError, Sorter
from sys import argv

def quit_with_usage():
    print('Usage: {} <default|merge|insertion|bubble>'.format(argv[0]))
    quit()

def main():
    # Check number of the arguments
    algo = 'default'
    if len(argv) == 2:
        algo = argv[1]
    elif len(argv) > 2:
        quit_with_usage()

    # Create a new Sorter object and set the algorithm
    sorter = Sorter()
    try:
        sorter.set_algorithm(algo)
    except AlgorithmNotImplementedError:
        print("No such algorithm: %s" % algo)
        quit_with_usage()

    # Doubling Test setting
    trials = 100
    n = 64

    print("# Perform a doubling test for {} sort with {} trials".format(algo, trials))
    print("starting with n = {}".format(n))

    # Time how long it takes to sort
    sorter.generate_new_tuple(n)
    previous = sorter.time_trials(trials)
    print('n: {0:7d} time: {1:7f} (n:n/2) ratio: -'.format(n, previous))

    while True:
        n *= 2
        sorter.generate_new_tuple(n)
        current = sorter.time_trials(trials)
        ratio = current / previous
        print('n: {0:7d} time: {1:7f} (n:n/2) ratio: {2:7f}'.format(n, current, ratio))
        previous = current

if __name__ == '__main__':
    main()
