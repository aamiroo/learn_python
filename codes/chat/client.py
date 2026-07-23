"""
peer to peer chat(p2p)
this is client
"""
from colorama import init, Fore #for show color in terminal

init(autoreset=True)
import socket

HOST = "192.168.100.35"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    print()
    msg = input((Fore.GREEN + "you: "))
    print()

    if not msg:
        break

    client.send(msg.encode())
    reply = client.recv(1024).decode()
    print(Fore.BLUE + f"server: {reply}")

client.close()
print(Fore.RED + f"{HOST} is out")
