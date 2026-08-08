"""
peer to peer chat(p2p)
this is server
"""
from colorama import init, Fore  # for show color in terminal

init(autoreset=True)  # Returning to the normal color state
import socket  # for socket
import threading  # For simultaneous chat

HOST = "0.0.0.0"  # IP for all Interface
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket & IP and TCP
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # To free up the port

server.bind((HOST, PORT))  # for conection Socket to IP

server.listen(1)  #For the number of connections that can be placed in the connection queue
print(Fore.GREEN + "Waiting for connection...")
client, address = server.accept()

print("Connected:", address)  # Show who is connected


# To receive the message
def receive():
    while True:
        try:
            data = client.recv(1024)  ## To receive the data from socket & 1024 Maximum number of bytes
            if not data:
                break
            print(f"\n{Fore.BLUE}server: {data.decode()}")
        except:
            break

# Create a separate thread and execute the `receive` function within it.
threading.Thread(target=receive, daemon=True).start()

try:
    while True:
        print()
        reply = input(Fore.GREEN + "you: ")  # for writing message
        print()

        if not reply:
            break

        client.send(reply.encode())
        
finally:
    client.close()
    print(Fore.RED + f"{address} is out")
    server.close()
