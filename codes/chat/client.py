"""
peer to peer chat(p2p)
this is client
"""
from colorama import init, Fore #for show color in terminal

init(autoreset=True)
import socket
import threading

HOST = "192.168.4.128"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            print(f"\n{Fore.BLUE}server: {data.decode()}")
        except:
            break
threading.Thread(target=receive, daemon=True).start()

while True:
    print()
    msg = input((Fore.GREEN + "you: "))
    print()

    if not msg:
        break

    client.send(msg.encode())
   
client.close()
print(Fore.RED + f"{HOST} is out")
