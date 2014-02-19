#!/usr/bin/env python

""" A simple echo server """ 

import socket

def data(x, y):
    data = ''
	while True:
		buff = x.recv(y)
		data += buff
		if not buff:
			return data

def echo_server():
	host = '' 
	port = 50001 
	backlog = 5 
	buffer_size = 32
	# ^ http://ilab.cs.byu.edu/python/socket/echoserver.html

	server_socket = socket.socket(
		socket.AF_INET,
		socket.SOCK_STREAM,
		socket.IPPROTO_IP)
	server_socket.bind((host, port))
	server_socket.listen(backlog)

	while True: 
		conn, addr = server_socket.accept() 
		conn.sendall(data(conn, buffer_size))
		conn.close()

	server_socket.close()

if __name__ == '__main__':
	echo_server()
