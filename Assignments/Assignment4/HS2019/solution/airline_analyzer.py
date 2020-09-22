# -*- coding: utf-8 -*-
"""
a4_task2.airline_analyzer
XX-YYY-ZZZ
<Your name>
"""

import networkx as nx
from a4_task2 import get_data, NoSuchFlight


def get_airlines_per_route(airlines_dict, source_airport_code, target_airport_code, max_hops):
    """
    Find airlines that have a path between the given airports.

    :param airlines_dict: a dictionary whose key is the airline code and the value is the airline object
    :param source_airport_code: the code of the source airport
    :param target_airport_code: the code of the target airport
    :param max_hops: the maximum number of hops allowed between the two airports.
    :return: a list of Airline objects serving the two airports within the maximum number of hops
    """
    ###   Task 2(c)   ###

    # Hint: use Airline's class method get_route() from 2(b)
    # ADD YOUR CODE HERE
    
    list_ = list()
    
    for airline in airlines_dict.items():
        
        
        try:
            route_ = airline[1].get_route(source_airport_code, target_airport_code)
            
            #As i understand it a hop is when we have to change the airplane (so starting and end airport dont count -> -2)
            if len(route_) - 2 <= max_hops:
                
                list_.append(airline[1])
        except:
            pass
    
    
    return list_

    ### Task 2(c) END ###


def find_most_connected_airport(airlines_dict):
    """
    Find the airport with the highest number of connections available and return its code.

    :param airlines_dict: a dictionary whose key is the airline code and the value is the airline object
    :return: the airport code with the highest number of connections available.
    """

    ###   Task 2(d)   ###

    # ADD YOUR CODE HERE
    
    dict_ = dict()
    
    for airline in airlines_dict.items():
        graph = airline[1].graph
        for node in graph:
            if node in dict_:
                connections_previous = dict_[node]
                connection_new = graph.degree(node)
                dict_[node] = connections_previous + connection_new
            else:
                dict_[node] = graph.degree(node)
                
      
    
    
    
    
    most_connected_airport = str()
    max_connections = 0
    
    
    for element in dict_.items():
    
        if element[1] > max_connections:
            
            most_connected_airport = element[0]
            max_connections = element[1]
            
            
    
    return str(most_connected_airport)
    
    

    ### Task 2(d) END ###


def main():
    airlines_dict, airports_dict = get_data()

    print("\n --------------- Airline Analyzer ---------------\n")
    print("# {} airlines are loaded with {} routes"
            .format(len(airlines_dict.keys()), sum([len(a.graph.edges) for a in airlines_dict.values()])))
    print("------")

    # Print a few airlines and their number of routes:
    print("# A few airlines and their number of routes:")
    some_airline_codes = ["AF", "LX", "FI"]
    for airline in airlines_dict.values():
        if airline.code in some_airline_codes:
            print(' - {} has {} routes'.format(airline.name, nx.number_of_edges(airline.graph)))

    print("------")


    # Airlines operating in "St Gallen Altenrhein Airport" (Airport code: "ACH")
    st_gallen_airport = "ACH"
    airlines_in_st_gallen = []
    for airline in airlines_dict.values():
        if airline.graph.has_node(st_gallen_airport):
            airlines_in_st_gallen.append(airline)
    print("# Airlines operating in {}:".format(st_gallen_airport))
    for airline in airlines_in_st_gallen:
        print(" - {}".format(airline))

    print("------")

# Uncomment this comment block after Task 2(b) #
    # Check if Swiss International Air Lines (id: 4559) operates in two airports
    swissair_id = 4559
    zurich_airport = "ZRH"
    destination_airports = ["NRT", "NUE", "YVR", "BAH"]
    print("# Check routes for {} from {}:".format(airlines_dict[swissair_id].name, airports_dict[zurich_airport]))
    for dst in destination_airports:
        try:
            route = airlines_dict[swissair_id].get_route(zurich_airport, dst)
            print(" - has a route to {}: {}".format(airports_dict[dst], '->'.join(route)))
        except NoSuchFlight:
            print(" - no route to {}".format(airports_dict[dst]))

    print("------")
# Comment block for Task 2(b) END #


# Uncomment this comment block after Task 2(c) #
    airlines_with_max_1_hop_LIS_to_NUE = get_airlines_per_route(airlines_dict, "LIS", "NUE", 1)
    print("# Airlines with max 1 connection from LIS to NUE")
    for airline in airlines_with_max_1_hop_LIS_to_NUE:
        print(" - {}".format(airline))

    print("------")
# Comment block for Task 2(c) END #


# Uncomment this comment block after Task 2(d) #
    print("# Most Connected Airport:")
    most_connected = find_most_connected_airport(airlines_dict)
    if most_connected in airports_dict:
        print(" - {}".format(airports_dict[most_connected]))
# Comment block for Task 2(d) END #


if __name__ == '__main__':
    main()
