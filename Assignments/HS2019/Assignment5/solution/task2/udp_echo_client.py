# -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # #
# # NO NEED TO BE CHANGED.  # #
# # # # # # # # # # # # # # # #
"""
task2.udp_echo_client
"""

from socket import socket, timeout, AF_INET, SOCK_DGRAM

SERVER_IP = "127.0.0.1" # IP address of the server
SERVER_PORT = 22222     # UDP Port of the server
BUF_SIZE = 1024         # Maximum receiving data buffer size in bytes
TIMEOUT = 0.5           # Timeout for receiving data in second

if __name__ == '__main__':
    print("\n --------------- UDP Echo Client ---------------\n")
    print("Type your message and hit [ENTER]")

    # Create a UDP socket at client side
    # AF_INET: IPv4
    # SOCK_DGRAM: UDP
    sock = socket(family=AF_INET, type=SOCK_DGRAM)

    # Set timeout for the connection
    sock.settimeout(TIMEOUT)

    # An infinite loop
    while True:
        # Prompt user to type a message
        msg = input("< ")
        # Encode the message string into a bytestring
        byte_data = msg.encode()
        # Send the byte_data to the server through the UDP socket
        sock.sendto(byte_data, (SERVER_IP,SERVER_PORT))
        # Receive data from the server if it's running
        try:
            data, server_address = sock.recvfrom(BUF_SIZE)
            print("{} > {}".format(server_address, data.decode()))
            if data.decode() == "BYE":
                break
        except timeout:
            print("-- The server was not reachable at <{}:{}> --".format(SERVER_IP,SERVER_PORT))
