#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:56:07 2024

@author: ranaemad
"""

from socket import *
from threading import *

host = '127.0.0.1'
port = 7006

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print(f"Server listening on {host}:{port}")

clients = []
nicknames = []


def broadcast_message(message, currentclient):
    for client in clients:
        try:
            if client != currentclient:
                client.send(message.encode('utf-8'))
        except:
            client.close()
            clients.remove(client)


def handle(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            broadcast_message(message, client)

        except KeyboardInterrupt:
            clients.remove(client)
            client.close()

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f'connection is established with {str(client_address)}')
    client_socket.send("nickname?".encode('utf-8'))
    nickname = client_socket.recv(2048).decode('utf-8')
    nicknames.append(nickname)
    print(f'The alias of this client is {nickname}')
    client_thread = Thread(target=handle, args=(client_socket,))
    client_thread.start()

server_socket.close()