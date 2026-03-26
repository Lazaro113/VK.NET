import socket
from colorama import Fore

print("")
host = input("Digite: ")
portas = [80, 443, 20, 21, 990, 22, 23, 25, 110, 143, 53]

try:
	with open("testelazaro.txt", "a") as f:
		f.write("\n" + "=" * 3 + "\n" + host + "\n")
		for ports in portas:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(2.0)
			code = s.connect_ex((host, ports))
			if code == 0:
		
				msg = f"[+] A porta {ports} está aberta"
				print(msg)
				f.write(msg)	
			else:
				msg = f"[-] A porta {ports} está fechada"
				print(msg)
				f.write(msg)
except Exception as e:
	print("Error: ", e)

