import socket
import sys

while True:
	ip = input("Digite seu Endereço/IP: ")
	print(ip, "===>", socket.gethostbyname(ip))
	input("Aperte Enter...")
	break
