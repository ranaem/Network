#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:47:44 2024

@author: ranaemad
"""

from socket import *

try:
    S = socket(AF_INET, SOCK_STREAM)

    host = '127.0.0.1'
    port = 7007

    S.connect((host, port))

    while True:

        # Send
        
        S.sendall(input("Client : ").encode('utf-8'))
        
        # Receive
        data = S.recv(2048).decode('utf-8')
        if not data:
            break
        if data.lower() == 'exit':
            break
        
        print(f"Server: {data}")
        
    S.close()
    
except error as e:
    print(e)
except KeyboardInterrupt:
    print("Server Stopped by the user")
