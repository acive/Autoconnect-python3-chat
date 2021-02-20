# coding: utf-8
import socket, os, sys
from multiping import multi_ping

mon_ip = socket.gethostbyname(socket.gethostname())
print("\nClient --- En attente d'un serveur...\n")
ips = []
def pcs_connectes():
	debut = mon_ip.split('.')[0] + '.' + mon_ip.split('.')[1] + '.' + mon_ip.split('.')[2] + '.'
	addrs = []
	for i in range(2,256):
		addrs.append(debut + str(i))
	ips_on, ips_off = multi_ping(addrs, timeout=1, retry=2)
	ips_ok = []
	for ip in ips_on:
		if ip != mon_ip:
			ips_ok.append(ip)
	return ips_ok

print('\nTentative de connexion aux adresses :')
print(pcs_connectes())
print()
connecte = False
while connecte == False:
	ips = pcs_connectes()
	for ip in ips:
		port = (int(ip.split('.')[0]) * int(ip.split('.')[1])) - int(ip.split('.')[3])
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(.5)
		try:
			sock.connect((ip, port))
			sock.send('?'.encode())
			sock.close()
			os.system('python cli_serv.py client ' + ip + ':' + str(port))
			connecte = True
		except:
			pass
	
