# -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # #
# # NO NEED TO BE CHANGED.  # #
# # # # # # # # # # # # # # # #

__all__ = ['Airline', 'NoSuchFlight', 'get_data']

import os
from pathlib import Path

from .airline import Airline, NoSuchFlight


def _iterate_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().replace('"', '')
            if len(line) == 0:
                continue
            yield line


def get_data():
    # Create a dict of all Airlines (Code -> Airline)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    airlines = {}
    for line in _iterate_file(Path(base_dir, "data", 'airlines.dat')):
        airline_data = line.split(',')
        # airline_data[0]: Airline ID; Unique OpenFlights identifier for this airline
        # airline_data[1]: Name of the airline
        # airline_data[3]: Airline CODE
        airline_id = int(airline_data[0])
        airline_name = airline_data[1]
        airline_code = airline_data[3]
        airlines[airline_id] = Airline(airline_name, airline_code)

    # Create a dict of all Airports (Code -> Airport)
    airports = {}
    for line in _iterate_file(Path(base_dir, 'data', 'airports.dat')):
        airport_data = line.split(',')
        # airport_data[0]: Airport ID; Unique OpenFlights identifier for this airport
        # airport_data[1]: Name; Name of the airport
        # airport_data[4]: Code: Code of the airport
        airport_name = airport_data[1]
        airport_code = airport_data[4]
        airports[airport_code] = airport_name

    # Fill data into the graph attribute (nx.Graph) of each airline object
    for line in _iterate_file(Path(base_dir, 'data', 'routes.dat')):
        route_data = line.split(',')
        # route_data[0]: Airline Code;
        # route_data[1]: Airline ID; Unique OpenFlights identifier for this airline
        # route_data[2]: Source airport Code
        # route_data[3]: Source airport ID
        # route_data[4]: Destination airport Code
        # route_data[5]: Destination airport ID
        try:
            airline_id = int(route_data[1])
            airline = airlines[airline_id]
            source_airport = route_data[2]
            target_airport = route_data[4]
            airline.graph.add_edge(source_airport, target_airport)
        except (ValueError, KeyError):  # Ignore unknown airlines/airports (e.g., '\\N')
            pass

    return airlines, airports
