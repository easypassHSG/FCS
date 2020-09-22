# -*- coding: utf-8 -*-
"""
oop_a3_t2
XX-YYY-ZZZ
<Your name>
"""

import networkx as nx


class Airline:
    def __init__(self, name, code):
        """
        Constructor of class Airline
        You do not need to change this method.
        """
        self.name = name
        self.code = code
        self.graph = nx.Graph()

    def __str__(self):
        """
        Method to convert this class to string.
        You do not need to change this.
        """
        return "{} - {}".format(self.code, self.name)

    def __repr__(self):
        """
        You do not need to change this method.
        """
        return self.__str__()

    def __hash__(self):
        """
        You do not need to change this method.
        """
        return hash(str(self))

    def __eq__(self, other):

        """
        You do not need to change this method.
        """
        return hash(self) == hash(other)

    def get_route(self, source, target):
        """
        Method to return the shortest route from the source airport to the target airport.
        :param source: source airport -> type Airport
        :param target: target airport -> type Airport
        :raise: NoSuchFlight if there is no route from the source to the target airport
        :return: Route from source airport to the target represented by the list of aiports from the source to the target.
        """
        ###   Task 2(b)   ###

        # TASK 2 (b) BEGIN
        # Note that this function raises a NoSuchFlight exception
        # if there is no route from the source airport to the target airport.
        # HINT: use nx.shortest_path() and handle the exceptions to raise NoSuchFlight
        # ADD YOUR CODE HERE
        
        
        try:
            
            return nx.shortest_path(self.graph, source, target)
            
        except:
            raise NoSuchFlight
        

        ### Task 2(b) END ###


class NoSuchFlight(Exception):
    """
    Raised when no such flight/route was found in the specified airline.
    You do not need to change this class.
    """
    pass
