# coding: utf-8
import socket, os, sys, psutil

mon_ip = socket.gethostbyname(socket.gethostname())
hote = sys.argv[2].split(':')[0]
port = int(sys.argv[2].split(':')[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def client():
	sock.settimeout(None)
	sock.connect((hote, port))
	os.system('cls') # 'cls' pour windows, 'clear' pour linux
	print('\nJe suis le client, mon Adresse est : ' + mon_ip)
	print('Connecté au serveur, adresse : ' + hote + ' sur le port : ' + str(port))
	print("*** Tapez 'exit' ou 'quit' pour quitter ***\n")
	print("En attente d'un message")
	sys.stdout.flush()
	while True:
		sys.stdout.flush()
		recu = sock.recv(1024).decode()
		if len(recu) > 0:
			print('Serveur : ', recu)
		else:
			print('Serveur : ?')
		if recu == 'exit' or recu == 'quit': break
		sys.stdout.flush()
		message = input("Client > ")
		if len(message) > 0:
			sock.send(message.encode())
		else:
			sock.send('?'.encode())
		print("message envoyé... attend la réponse")
		if message == 'exit' or message == 'quit': break
	sock.close()

def serveur():
	sock.settimeout(None)
	sock.bind(('', port))
	sock.listen(1)
	client, address = sock.accept()
	os.system('cls') # 'cls' pour windows, 'clear' pour linux
	print('\nJe suis le serveur, mon Adresse est : ' + mon_ip)
	print('Connecté au client, adresse : ' + str(address[0]) + ' sur le port : ' + str(port))
	print("*** Tapez 'exit' ou 'quit' pour quitter ***\n")
	sys.stdout.flush()
	while True:
		sys.stdout.flush()
		message = input('Serveur > ')
		if len(message) > 0:
			client.send(message.encode())
		else:
			client.send('?'.encode())
		print('Message envoyé... attend la réponse')
		if message == 'exit' or message == 'quit': break
		sys.stdout.flush()
		recu = client.recv(1024).decode()
		if len(recu) > 0:
			print('Client : ' + recu)
		else:
			print('Client : ?')
		sys.stdout.flush()
		if recu == 'exit' or recu == 'quit': break
	client.close()
	sock.close()

pid = os.getpid()
for processus in psutil.process_iter():
	if 'python.exe' in str(processus).lower():
		if processus.pid != pid:
			processus.terminate()

if sys.argv[1] == 'client':
	client()
else:
	serveur()

