#!/usr/bin/env python

""" A simple echo client """ 

import socket
import sys
import echo_server

def echo_client(message):
    host = 'localhost' 
    port = 50001 
    buffer_size = 32
    # ^ http://ilab.cs.byu.edu/python/socket/echoclient.html

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    client_socket.connect((host, port))

    client_socket.sendall(message)
    client_socket.shutdown(socket.SHUT_WR)
    data = echo_server.data(client_socket, buffer_size) 
    client_socket.close()
    return data

if __name__ == '__main__':
    print echo_client(str(sys.argv[1]))
