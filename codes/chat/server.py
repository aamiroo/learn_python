"""
peer to peer chat(p2p)
this is server
"""
from colorama import init, Fore  # for show color in terminal

init(autoreset=True)
import socket  # for socket

HOST = "0.0.0.0"  # IP for all Interface
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IP and TCP
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # To free up the port
server.bind((HOST, PORT))  # for conection Socket to IP
server.listen(1)
print(Fore.GREEN + "Waiting for connection...")
client, address = server.accept()

print("Connected:", address)

try:
    while True:
        print()
        msg = client.recv(1024).decode()
        if not msg:
            break
        print(Fore.BLUE + f"client: {msg}")
        print()

        reply = input((Fore.WHITE + "you: "))
        client.send(reply.encode())
finally:
    client.close()
    print(Fore.RED + f"{address} is out")
    server.close()
