import os
import sys
import subprocess

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
	print("( 1 ) - Nmap")
	print("( 2 ) - Whois")
	print("( 3 ) - OpenVAS")
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

while True:
	clear()
	main()
	vk_menu()
	sub = int(input("Escolha: "))
	
	if sub == 1:
		while True:
			clear()
			main()
			vk_vul()
			sub = int(input("Escolha: "))
			
			if sub == 10:
				break
	
	elif sub == 2:
		while True:
			clear()
			main()
			vk_atk()
			sub = int(input("Escolha: "))
			
			if sub == 10:
				break

	elif sub == 3:
		while True:
			clear()
			main()
			vk_scan()
			sub = int(input("Escolha: "))
			
			if sub == 1:
				os.system('chmod +x utils/scanners/nmap.sh')
				while True:
					clear()
					main()
					retorno = os.system('utils/scanners/nmap.sh')
					if retorno == 0:
						break

			elif sub == 10:
				break

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
