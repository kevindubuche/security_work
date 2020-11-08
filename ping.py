#!/usr/bin/env python3

# ----------------------------------------
# Program  : Efectuer un ping vers le IP d'un server qui ecoute au port 6332
# FileName : ping.py
# Input	  : 127.0.0.1
# Output	  :  
# By       : Kevin J. DUBUCHE 
# ---------------------------------------- 

# Ecrire un programme en python qui permet d'effectuer un ping
# Contraintes: Port 6332  | use Idle | use socket | architecture Client/Server  

# __________________________________________________________

#importation des packages utiles a programme
import socket
from datetime import datetime
#fin des importations

IP = input("Enter the IP address: ")
t1 = datetime.now()
ttl = 1
PORT = 6332

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(ttl)
   result = s.connect_ex((addr,PORT))
   if result == 0:
      return 1
   else :
      return 0

def ping(addr):
      if (scan(addr)):
         t2 = datetime.now()
         total = t2 - t1
         print('Succes !!')
         print ("from {}: ttl={} time={} ".format(addr,ttl,total))
      else:
          print('Port unreachable')

      
ping(IP)