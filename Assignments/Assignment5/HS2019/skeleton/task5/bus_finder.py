# -*- coding: utf-8 -*-
"""
task4.bus_finder
XX-YYY-ZZZ
<Your name>
"""
from datetime import datetime, tzinfo, timedelta
import requests

class Bus:
    '''Bus class'''
    def __init__(self, operator, number, departure_time, arrival_time):
        '''
        Bus constructor

        :param operator: a string that contains the name of the operator (e.g., "VBSG")
        :param number: a integer that contains the number of the bus (e.g., 5)
        :param departure_time: a datetime object to indicate the departure time
        :param arrival_time: a datetime object to indicate the arrival time
        '''
        self.operator = operator
        self.number = number
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __str__(self):
        return "[{} #{}] {}->{}".format(self.operator,
                self.number,
                self.departure_time.astimezone(tz=CET()).strftime('%H:%M:%S'),
                self.departure_time.astimezone(tz=CET()).strftime('%H:%M:%S'))


class CET(tzinfo):
    '''datetime.tzinfo CET class for Swiss timezone'''
    def utcoffset(self, dt):
        return timedelta(hours=+2)

    def tzname(self, dt):
        return "CET"

    def dst(self, dt):
        return timedelta(hours=+2)


def get_location_name(location_id):
    '''
    Send an HTTP GET request to http://transport.opendata.ch/v1 API
    to get the name for the location ID

    :param location_id: a string that contains the location ID
    :return: a string with the location name
    '''
    ###   Task 5(a)   ###

    # HINT1: the relative URI '/locations' has a request parameter 'query'.
    # Pass the location_id as a query parameter, for instance (you can try this URI in your Web browser):
    # https://transport.opendata.ch/docs.html#locations?query=8589637
    #
    # HINT2: The 'name' of the location is inside the first object in the 'stations' list returned in the HTTP response.
    #
    # ADD YOUR CODE HERE

    ### Task 5(a) END ###


def find_next_bus(origin, destination, time, limit=5):
    '''
    Send an HTTP GET request to http://transport.opendata.ch/v1 API
    to find next buses from point of origin to destination at the time.
    This function can assume there is only one 'section' to reach
    the destination from the origin:
    https://transport.opendata.ch/docs.html#section

    :param origin: a string that contains the departing station/stop's ID
    :param destination: a string that contains the destination station/stop's ID
    :param timestamp: a datetime object to indicate the time to look up from
    :param limit: an integer to indicate the number of busses to find
    :return: a list of Bus objects
    '''
    ###   Task 5(b)   ###

    # HINT 1: /connections has request parameters 'date' and 'time'; use strftime() to format the parameter
    # https://transport.opendata.ch/docs.html#connections
    # https://docs.python.org/3/library/datetime.html#datetime.date.strftime
    # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    # e.g.,) datetime.date(2019, 10, 16).strftime('%d-%m-%Y') == "16-10-2019"
    #
    # HINT 2: use datetime.fromtimestamp() to convert a timestamp to a datetime object
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp
    #
    # ADD YOUR CODE HERE

    ### Task 5(b) END ###


def main():
#''' # Uncomment this comment block after Task 5(a)
    # Set the points of origin and destination
    origin =      "8574095" # Location ID: St. Gallen, Bahnhof
    destination = "8589637" # Location ID: St. Gallen, Uni/Dufourstrasse

    # Get the location names
    origin_name = get_location_name(origin)
    destination_name = get_location_name(destination)
    print("# Find th next bus from {} to {}".format(origin_name, destination_name))
#''' # Comment block for Task 5(a) END

#''' # Uncomment this comment block after Task 5(b)
    # Find the next 5 buses from Banhof to Uni/Dufourstrasse
    next_buses = find_next_bus(origin, destination, datetime.now())
    for b in next_buses:
        print(b)
#''' # Comment block for Task 5(b) END


if __name__ == '__main__':
    main()
