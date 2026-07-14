#!/usr/bin/python
import socket,sys

ip = input("Digite o Endereço: ")

while True:
	try:
		for porta in range(1, 65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(5)
			if s.connect_ex((ip, porta)) == 0:
				print("porta", porta, "aberta")
				s.close()
				
	except KeyboardInterrupt:
		print(" Error ou Fechado ").strip()
		break
	input("Aperte Enter... ")	
	break
