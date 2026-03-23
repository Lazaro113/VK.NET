echo
echo "( 1 ) NMAP - Varredura"
echo "( 2 ) NMAP - Expecifica/Todas"
echo "( 3 ) NMAP - Varredura"
echo "( 0 ) Sair"

echo




read -p "Escolha: " escolha

if [ "$escolha" = 1 ]; then
	clear
 	read -p "Digite seu ip: (Formato: 192.168.0.0/24) " sub
	nmap -sp "$sub"

elif [ "$escolha" = 2 ]; then
	clear 
	read -p "Digite seu ip: " sub
	read -p "Digite a porta: " sub2
	nmap -p "$sub2" "$sub"

elif [ "$escolha" = 10 ]; then 
	exit 0


fi
