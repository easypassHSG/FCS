# -*- coding: utf-8 -*-
"""
task2.udp_echo_server
XX-YYY-ZZZ
<Your name>
"""

from socket import socket, timeout, AF_INET, SOCK_DGRAM

SERVER_IP = "127.0.0.1" # IP address of the server
SERVER_PORT = 22222     # UDP Port of the server
BUF_SIZE = 1024         # Maximum receiving data buffer size in bytes

class UDPEchoServer:
    """
    An echo sever with UDP transport.
    """

    def __init__(self, ip_address, udp_port):
        """
        :param ip_address: the IP address to listen
        :param udp_port: the port to listen for the udp connection
        """
        self.ip_address = ip_address
        self.udp_port = udp_port

        # Create a UDP socket at client side
        # AF_INET: IPv4
        # SOCK_DGRAM: UDP
        self._sock = socket(family=AF_INET, type=SOCK_DGRAM)

    def start(self):
        """
        Start the UDP Echo Server.

        This class instance method first binds the socket to the IP address and the port.
        Then in an infinite loop:
            1. Receive the data from clients
            2. Decode the received bytes object to a string message
            3. Print the message
            4. Make all the characters in the message to uppercase
            5. Encode the message to a bytes object
            6. Echo back the message to the client
            7. When the message from the client is 'bye', this echo server should exit the loop after sending back the last message (i.e., 'BYE') to the client.
        """
        print("\n --------------- UDP Echo Server ---------------\n")
        ###   Task 2(b)   ###

        # HINT 1: use self._sock.bind() to bind the IP address and the port.
        # Note that the address parameter of bind() is a tuple of an IP address (string) and Port (integer) for AF_INET address family.
        # https://docs.python.org/3/library/socket.html#socket.socket.bind
        #
        # HINT 2: use bytes.decode() to decode the data.
        # https://docs.python.org/3/library/stdtypes.html#bytes.decode
        # Don't forget to encode the data before sending it to the client!

        ### Task 2(b) END ###

if __name__ == '__main__':
    server = UDPEchoServer(SERVER_IP, SERVER_PORT)
    server.start()
