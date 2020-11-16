#!/usr/bin/env python3

# ----------------------------------------
# Program  : Scann ports & get the banners
# FileName : port_sweep.py
# Input	   : 127.0.0.1
# Output   : ref image or CSV file
# By       : Kevin J. DUBUCHE 
# ---------------------------------------- 

# __________________________________________________________

import socket # to manage socket --> IP:port
import os  #provides functions for interacting with the operating system
import csv  #CSV (Comma Separated Values) format for spreadsheets and databases

dictionnaire_contenant_output_du_fichier_csv = {}
liste_representant_un_nouveau_tuple=[]
port_de_depart = 1
port_d_arrive = 1024
def scanner_les_ports(adresse_ip_du_server_cible):
 try:
    for port in range(port_de_depart, port_d_arrive):
        socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = socket_object.connect_ex((adresse_ip_du_server_cible,port))
        if result == 0:
            liste_representant_un_nouveau_tuple =[]
            banner = recuperation_de_banner(adresse_ip_du_server_cible,port)
            domain = socket.gethostbyaddr(adresse_ip_du_server_cible)[0]
            service =str(socket.getservbyport(port))
            print ("Open socket detected: {}:{} \t-- Service: {} \t-- Hostname: {} \t--Banner: {}" .format(adresse_ip_du_server_cible,port,service,domain, banner)) 
            liste_representant_un_nouveau_tuple.append(str(adresse_ip_du_server_cible)) 
            liste_representant_un_nouveau_tuple.append(str(service))
            liste_representant_un_nouveau_tuple.append(str(domain))
            liste_representant_un_nouveau_tuple.append(str(banner))
            dictionnaire_contenant_output_du_fichier_csv[port] = liste_representant_un_nouveau_tuple
 
 except socket.error:
     pass
 finally:
        socket_object.close()

def recuperation_de_banner(adresse_ip_du_server_cible,port):
        print( "Tentative d acceder au banner du port: ", port)
        objet_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       
        try:
            objet_socket.connect((adresse_ip_du_server_cible, port))
            objet_socket.send('GET HTTP/1.1 \r\n')
            banner = objet_socket.recv(100)
            objet_socket.close()
            return banner
        except:
             return "Banner introuvable !!"

def generation_du_fichie_csv(dictionnaire_contenant_output_du_fichier_csv):
      csv_columns = ['Port', 'IP', 'Service', 'Domain', 'Banner']
      with open('rapport_du_port_sweep.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for key in dictionnaire_contenant_output_du_fichier_csv.keys():
            f.write("%s, %s, %s, %s, %s\n" % (key, dictionnaire_contenant_output_du_fichier_csv[key][0], dictionnaire_contenant_output_du_fichier_csv[key][1], dictionnaire_contenant_output_du_fichier_csv[key][2], dictionnaire_contenant_output_du_fichier_csv[key][3]))
      print('File rapport_du_port_sweep.csv generated successuffly !!')
if __name__ == "__main__":
    adresse_ip_du_server_cible = input('Enter the server IP : ')
    scanner_les_ports(adresse_ip_du_server_cible)
    print(dictionnaire_contenant_output_du_fichier_csv)
    generation_du_fichie_csv(dictionnaire_contenant_output_du_fichier_csv)
  