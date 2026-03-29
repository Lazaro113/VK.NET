import socket
from colorama import init, Fore

print("")
host = input("Digite: ")
print("")
print("Resultado: utils/scanners/port_scanner.txt")
portas = [80, 443, 20, 21, 990, 22, 23, 25, 110, 143, 53]
caminho = "utils/scanners/port_scanner.txt"

try:
	with open(caminho, "a") as f:
		f.write("\n" + "=" * 3 + "\n" + host + "\n")
		for ports in portas:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(2.0)
			code = s.connect_ex((host, ports))
			if code == 0:
				init()
				print("")
				msg = Fore.GREEN + f"[+] A porta {ports} está aberta"
				print(msg)
				f.write(msg)	
			else:
				init()
				print("")
				msg = Fore.RED + f"[-] A porta {ports} está fechada"
				print(msg)
				f.write(msg)
except Exception as e:
	print("Error: ", e)

