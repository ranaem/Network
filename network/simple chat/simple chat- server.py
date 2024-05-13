#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:22:13 2024

@author: ranaemad
"""

from socket import *

try:
    S = socket(AF_INET,SOCK_STREAM)
    S.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
    
    host = '127.0.0.1'
    port = 7007  
    S.bind((host,port))
    S.listen(5)
    
    print(f"Server listening on {host}:{port}")
    
    session, addr = S.accept()
    
    print(f"Connection from {addr[0]}")
    
    while True: 
        # Receive
        data = session.recv(2048).decode('utf-8')
        if not data:
            break
        
        if data.lower() == 'exit':
            break
        
            
        print(f"Client : {data}")

        # Send
        session.sendall(input("Server : ").encode('utf-8'))
        
    
    session.close()

except error as e:
    print(e)
except KeyboardInterrupt:
    print("Server Stopped by the user")
    
    