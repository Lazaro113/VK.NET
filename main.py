import os
import sys
import subprocess
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meu_ip = socket.gethostbyname(socket.gethostname())

def clear():
	os.system("clear")

def captcha():
	clear()
	input("Aperte Enter...")
	clear
	
captcha()	

def main():
	print("=================================================")
	print("")
	print("██╗   ██╗██╗  ██╗   ███╗   ██╗███████╗████████╗")
	print("██║   ██║██║ ██╔╝   ████╗  ██║██╔════╝╚══██╔══╝")
	print("██║   ██║█████╔╝    ██╔██╗ ██║█████╗     ██║   ")
	print("╚██╗ ██╔╝██╔═██╗    ██║╚██╗██║██╔══╝     ██║   ")
	print(" ╚████╔╝ ██║  ██╗██╗██║ ╚████║███████╗   ██║   ")
	print("  ╚═══╝  ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ")
	print("")
	print("=================================================") 
	print("")
	print(f"Conectado: {meu_ip}")  
 
		
def vk_menu():
	print("")
	print("( 1 ) - Vulnerabilidades")
	print("( 2 ) - Ataques")
	print("( 3 ) - Scanners")
	print("( 4 ) - Virús")
	print("( 0 ) - Sair")
	print("( 10 ) - Voltar")
	print("")
	
def vk_vul():
	print("")
	print("( 1 ) - Brute Force")
	print("( 2 ) - Web")
	print("( 3 ) - Wifi")
	print("( 4 ) - Exploits")
	print("( 0 ) - Sair")
	print("( 10 ) - Voltar")
	print("")

def vk_atk():
	print("")
	print("( 1 ) - DDoS")
	print("( 2 ) - Phishing")
	print("( 3 ) - Ransomware")
	print("( 0 ) - Sair")
	print("( 10 ) - Voltar")
	print("")
	
def vk_scan():
	print("")
	print("( 1 ) - PortScanner")
	print("( 2 ) - Whois")
	print("( 3 ) - IP/Site")
	print("( 0 ) - Sair")
	print("( 10 ) - Voltar")
	print("")

def vk_virus():
	print("")
	print("( 1 ) - Keylogger")
	print("( 2 ) - Ransomware")
	print("( 3 ) - Backdoor")
	print("( 0 ) - Sair")
	print("( 10 ) - Voltar")
	print("")


#SISTEMA DE MENU ============================================
while True:
	clear()
	main()
	vk_menu()
	sub = int(input("Escolha: "))
	
#SISTEMA DE VULNERABILIDADES

	if sub == 1:
		while True:
			clear()
			main()
			vk_vul()
			sub = int(input("Escolha: "))
			
			if sub == 10:
				break
#SISTEMA DE ATAQUES ============================================

	elif sub == 2:
		while True:
			clear()
			main()
			vk_atk()
			sub = int(input("Escolha: "))
			
			if sub == 10:
				break
#SISTEMA DE SCANNERS ============================================

	elif sub == 3:
		while True:
			clear()
			main()
			vk_scan()
			sub = int(input("Escolha: "))
			
			if sub == 1:
				while True:
					clear()
					main()
					retorno = os.system('python3 utils/scanners/portscanner.py')
					if retorno == 0:
						break
			if sub == 3:
				while True:
					clear()
					main()
					os.system('python3 utils/scanners/simple_scanner.py')
					break
                        
			elif sub == 10:
				break
#SISTEMAS DE MALWARES ============================================

	elif sub == 4:
		while True:
			clear()
			main()
			vk_virus()
			sub = int(input("Escolha: "))
			
			if sub == 10:
				break


	elif sub == 0:
		clear()
		print("")
		print("Saindo... Tchau até mais ;>")
		print("")
		sys.exit()
