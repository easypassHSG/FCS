# -*- coding: utf-8 -*-
"""
a4_task1.movie_analyzer
XX-YYY-ZZZ
<Your name>
"""

import networkx as nx

from a4_task1 import load_movies_as_graph, Movie


def get_list_of_performers(g, movie):
    """
    Get a list of performers.

    :param g: a networkx.Graph object that stores movie titles and its performers as nodes.
    :param title: a string contains the movie title. (e.g., "Hitchhiker's Guide to the Galaxy, The (2005)" or "All or Nothing (2002 I)".)
    :return: a list of string values that are the names of the performers who appeared in the movie.
    """
    ###   Task 1(b)   ###

    # HINT: use nx.all_neighbors()
    # https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.classes.function.all_neighbors.html
    # Remember to return the list!
    # ADD YOUR CODE HERE

    ### Task 1(b) END ###


def get_list_of_movies(g, performer):
    """
    Get a list of movie titles.

    :param g: a networkx.Graph object that stores movie titles and its performers as nodes.
    :param performer: a string contains the name of the performer. (e.g., "Affleck, Ben" or "Stojanovich, Christina (I)")
    :return: a list of string values that are the movie titles in which the performer appeared.
    """
    # ##   Task 1(c)   ## #

    # Remember to return the list!
    # ADD YOUR CODE HERE

    # ## Task 1(c) END ## #


def get_number_of_appearance_dict(g):
    """
    Get a dictionary for number of appearance of performers.

    :param g: a networkx.Graph object that stores movie titles and its performers as nodes.
    :return: a dictionary with integer keys and list of strings as values

    The get_number_of_appearance_dict() function creates a dictionary with
    the number of appearances in movies (integer) as its keys and
    list of performers (string) as its values, then it returns the dictionary.

    e.g.) Danny Devito and Sean Connery have appeared in 39 movies.
    # dct = get_number_of_appearance_dict(g)
    # print(dct[39])
    ['DeVito, Danny', 'Connery, Sean']
    """
    # ##   Task 1(d)   ## #

    # HINT: use insinstance() with Movie class to check if the node is a Movie object (or not)
    # Remember to return the dictionary!
    # ADD YOUR CODE HERE

    # ## Task 1(d) END ## #


def main():
    # Initialize an empty networkx.Graph object
    graph = load_movies_as_graph()
    print("# The graph has {} nodes with {} edges".format(len(graph.nodes), len(graph.edges)))
    print("------")


""" # Uncomment this comment block after Task 1(b) #
    # Find a list of performers who appeared in the movie
    hgg = Movie("Hitchhiker\'s Guide to the Galaxy, The (2005)")
    print('\nThe performers in {}'.format(hgg))
    performers = get_list_of_performers(graph, hgg)
    for p in performers:
        print('    - {}'.format(p))

    print("------")
""" # Comment block for Task 1(b) END #


""" # Uncomment this comment block after Task 1(c) #
    # Find a list of movies that the performer appeared
    print('\nThe movies Meryl Streep appeared:')
    ms_movies = get_list_of_movies(graph, "Streep, Meryl")
    for m in ms_movies:
        print('    - {}'.format(m))

    print("------")
""" # Comment block for Task 1(c) END #


""" # Uncomment this comment block after Task 1(d) #
    # Get a dictionary for appearance count
    noa_dict = get_number_of_appearance_dict(graph)

    # Print performers who appeared in 37-4 2movies
    for freq in range(37, 42):
        if freq not in noa_dict:
            print("No such performer.")
        else:
            print("Performers who acted in {} movies:".format(freq))
            for p in noa_dict[freq]:
                print("    - {}".format(p))

        print("---")

    # Find how many performers only appeared in one movie
    print("\nNumber of performers who have appeared in only one movie: {}".format(len(noa_dict[1])))
""" # Comment block for Task 1(d) END #


if __name__ == '__main__':
    main()
