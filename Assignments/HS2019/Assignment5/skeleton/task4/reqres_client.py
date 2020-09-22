# -*- coding: utf-8 -*-
"""
task4.reqres_client
XX-YYY-ZZZ
<Your name>
"""
import requests

REQRES_USERS_ENDPOINT = "https://reqres.in/api/users"
REQRES_USER_NOTFOUND = "https://reqres.in/api/users/23"
REQRES_POST_UNSUCCESSFUL = "https://reqres.in/api/login"

class User:
    '''User class for Reqres'''
    def __init__(self, first_name, last_name, email, user_id=None):
        '''
        User constructor

        :param first_name: a string that contains the user's first name.
        :param last_name: a string that contains the user's last name.
        :param email: a string that contains the user's email address.
        :param user_id: an integer that contains the user's ID, default is None.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if user_id is not None and not isinstance(user_id, int):
            raise AttributeError
        self.id = user_id

    def __str__(self):
        return "User[{}] {} {} <{}>".format(self.id, self.first_name, self.last_name, self.email)

    def assign_id(self, user_id):
        '''Assign an ID to the user'''
        if not isinstance(user_id, int):
            raise AttributeError
        self.id = user_id


def query_user_list(url):
    '''
    Send an HTTP GET request to https://reqres.in/api/users
    and return a list of User objects retrieved from the Reqres API.

    :param url: a string that contains the URL to be used in your HTTP GET request
    :return: a list of User objects if the status code of the HTTP response is 200.
    Otherwise, it should return None.
    '''
    ###   Task 4(a)   ###

    # HINT 1: use json() to parse the JSON response body to a dictionary object
    # https://requests.kennethreitz.org/en/master/user/quickstart/#json-response-content
    #
    # HINT 2: The list of users is stored at the 'data' key in the response payload.
    # You should instantiate a User object for each user
    #
    # ADD YOUR CODE HERE

    ### Task 4(a) END ###


def create_new_user(url, user):
    '''
    Send an HTTP POST request to https://reqres.in/api/users
    to create a new user from the 'user' object passed as a parameter/argument to this function.

    :param url: a string that contains the URL to be used in your HTTP POST request
    :param user: a new user to be created, the id instance attribute should be None
    :return: a tuple with the newly created user's 'id' (int) and 'createdAt' value (string) if the HTTP status code is 201.
    Otherwise, it should return the tuple (None, None)
    '''
    ###   Task 4(b)   ###

    # HINT: Reqres generates an 'id' for each newly created user,
    # and that 'id' is a string. The id attribute of User class should be an integer.
    # Don't forget to return an int for the id!
    #
    # ADD YOUR CODE HERE

    ### Task 4(b) END ###


def main():
''' # Uncomment this comment block after Task 4(a)
    print('# Retrieve users from Reqres')

    # Test the http status code handling
    if query_user_list(REQRES_USER_NOTFOUND) is not None:
        quit()

    # Retrieve the list of users
    users = query_user_list(REQRES_USERS_ENDPOINT)
    for u in users:
        if isinstance(u, User):
            print(u)
''' # Comment block for Task 4(a) END

''' # Uncomment this comment block after Task 4(b)
    print('\n# Create a new user on Reqres')
    new_user = User('John', 'Smith', 'jsmith@example.com')

    # Test the http status code handling
    new_id, created_at = create_new_user(REQRES_POST_UNSUCCESSFUL, new_user)
    if new_id is not None or created_at is not None:
        quit()

    # Create a new user
    new_id, created_at = create_new_user(REQRES_USERS_ENDPOINT, new_user)
    new_user.assign_id(new_id)
    print('A new user is created at {}:\n{} '.format(created_at, new_user))
''' # Comment block for Task 4(b) END


if __name__ == '__main__':
    main()
