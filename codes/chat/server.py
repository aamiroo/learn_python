"""
peer to peer chat(p2p)
this is server
"""
from colorama import init, Fore  # for show color in terminal

init(autoreset=True)
import socket  # for socket
import threading

HOST = "0.0.0.0"  # IP for all Interface
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IP and TCP
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # To free up the port
server.bind((HOST, PORT))  # for conection Socket to IP
server.listen(1)
print(Fore.GREEN + "Waiting for connection...")
client, address = server.accept()

print("Connected:", address)
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

try:
    while True:
        print()
        reply = input(Fore.GREEN + "you: ")
        print()

        if not reply:
            break

        client.send(reply.encode())
finally:
    client.close()
    print(Fore.RED + f"{address} is out")
    server.close()
