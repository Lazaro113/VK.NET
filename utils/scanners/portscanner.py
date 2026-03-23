import socket
from colorama import Fore

print("")
host = input("Digite: ")
portas = [80, 443, 20, 21, 990, 22, 23, 25, 110, 143, 53]


try:
	for ports in portas:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5.0)
		code = s.connect_ex((host, ports))
		if code == 0:
			
			print(Fore.GREEN + "[+] A porta", ports, "está aberta")
			
			
		else:
			print(Fore.RED + "[-] A porta", ports, "está fechada")
			
except Exception as e:
	print("Error", e)
			
		

