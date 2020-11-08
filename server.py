#!/usr/bin/env python3

# ----------------------------------------
# Program  : Initialiser un server et le laisser en ecoute sur le port 6332
# FileName : seerver.py
# Input	   : 
# Output   : The server [127.0.0.1] starts & is listening on port 6332
# By       : Kevin J. DUBUCHE 
# ---------------------------------------- 


# __________________________________________________________

#La premiere ligne(shebang) indique au compilateur ou trouver le variable d'environnement pour executer ce programme
import socket

HOST = '127.0.0.1'      # Standard loopback interface address (localhost)
PORT = 6332             # Port to listen on (non-privileged ports are > 1023). port should be an integer from 1-65535

# socket.socket() creates a socket object that supports the context manager type, 
# so you can use it in a with statement. There’s no need to call s.close():
#AF_INET,specify the address family and socket type (IPv4)
#SOCK_STREAM is the socket type for TCP
#listen()It specifies the number of unaccepted connections that the system will allow before refusing new connections.
#accept() blocks and waits for an incoming connection.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Succes !!')
    print('The server ['+HOST+'] starts & is listening on port '+str(PORT))
    conn, addr = s.accept()
    with conn: #on s'aassure de fermer la connection apres la reception de la requette
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)