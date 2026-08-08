"""
peer to peer chat(p2p)
this is client
"""
from colorama import init, Fore #for show color in terminal

init(autoreset=True) # Returning to the normal color state
import socket  # for connection
import threading  # For simultaneous chat

HOST = "192.168.4.128"  # ip server
PORT = 5000  

# function connection
def connect_to_server(host,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creat socket with IP v4 & tcp mode
    client.connect((host,port)) # Socket connection to destination
    return client

client = connect_to_server(HOST, PORT) # Create connection

# To receive the message
def receive():
    while True:
        try:
            data = client.recv(1024)  # To receive the data from socket & 1024 Maximum number of bytes
            if not data:
                break
            print(f"\n{Fore.BLUE}server: {data.decode()}")   # Converting Byte to String
        except:
            break

# Create a separate thread and execute the `receive` function within it.
threading.Thread(target=receive, daemon=True).start()   

while True:
    print()
    msg = input((Fore.GREEN + "you: ")) # for writing message
    print()

    if not msg:
        break

    client.send(msg.encode())
   
client.close()
print(Fore.RED + f"{HOST} is out")
