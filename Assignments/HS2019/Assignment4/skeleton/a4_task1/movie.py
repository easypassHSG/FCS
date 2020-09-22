# -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # #
# # NO NEED TO BE CHANGED.  # #
# # # # # # # # # # # # # # # #

import networkx as nx
from os import path
from pathlib import Path

class Movie:
    def __init__(self, title):
        self.title = title
        pi = title.rfind("(")
        self.year = int(title[pi + 1:pi + 5])

    def __str__(self):
        return "{}".format(self.title)

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return hash(self) == hash(other)


def load_movies_as_graph():
    # Initialize an empty networkx.Graph object
    graph = nx.Graph()

    # Get the absolute path for the current directory
    base_dir = path.dirname(path.abspath(__file__))
    # Open the file movies.txt in the data directory with 'R'ead mode
    with Path(base_dir, 'data', 'movies.txt').open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                # Split the line by the delimiter '/'
                movie_info = line.split('/')
                # movie_info[0]: Title of the movie followed by the year
                # movie_info[1:]: List of performers appeared in the movie
                title = movie_info[0]
                performers = movie_info[1:]

                # Create a Movie object
                movie = Movie(title)
                for p in performers:
                    # Add an edge for the movie title and each performer
                    graph.add_edge(movie, p)
    return graph
