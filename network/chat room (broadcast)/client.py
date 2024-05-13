#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:59:08 2024

@author: ranaemad
"""

from socket import *
import threading

host = '127.0.0.1'
port = 7006
nickname = input("What is your nickname: ")
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))



def receive_messages():
    global quite, nickname
    while True:
        recv_data = client_socket.recv(1024).decode('utf-8')
        # print(message)

        if recv_data == "nickname?":
            client_socket.send(nickname.encode('utf-8'))
        elif recv_data == f'{nickname}:{quite}':
            return
        else:
            print("")
            print(recv_data)


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    sent_data = f'{nickname}:{input("")}'
    quite = "bye"
    if sent_data == f'{nickname}:{quite}':
        client_socket.send(sent_data.encode("utf-8"))
        break
    client_socket.send(sent_data.encode('utf-8'))

client_socket.close()