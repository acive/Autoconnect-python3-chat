import socket, os
print("\nServeur --- En attente d'un client...\n")
ip = socket.gethostbyname(socket.gethostname())
port = (int(ip.split('.')[0]) * int(ip.split('.')[1])) - int(ip.split('.')[3])
ip += ':' + str(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
while True:
	sock.listen(1)
	client, address = sock.accept()
	response = client.recv(1024).decode()
	if response != '': break
client.close()
sock.close()
os.system('python cli_serv.py serveur ' + ip)
