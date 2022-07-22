import random
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
IP_address = "127.0.0.1"
Port = 55555

# creating the server
server.bind((IP_address, Port))
server.listen(1)

# waiting for client
print("\nServer Started")
print("connecting to the client...")
conn, addr = server.accept()
print("Client has Connected\n\n")

# Getting P
print("Receiving Public Key from Client")
P = conn.recv(2048)
if P:
	P = int(P.decode('utf-8'))

# Getting E1
E1 = conn.recv(2048)
if E1:
	E1 = int(E1.decode('utf-8'))

# Getting E2
E2 = conn.recv(2048)
if E2:
	E2 = int(E2.decode('utf-8'))
print(f"Received public key is {P},{E1} and {E2}")
PT = int(input("Enter the Plain Text: \n"))
R = random.randint(0,P-2)
C1 = (E1**R)%P
C2 = (PT*(E2**R))%P
print("R : ",R)
print("C1 : ",C1)
print("C2 : ",C2)
print("Sending Ciphertext to the client")
# sending C1 and C2
conn.send(bytes(str(C1),'utf-8'))
conn.send(bytes(str(C2),'utf-8'))


conn.close() 
server.close()
# Server Started
# connecting to the client...
# Client has Connected
#
#
# Receiving Public Key from Client
# Received public key is 1597,315 and 1586
# Enter the Plain Text:
# 100
# R :  1227
# C1 :  1565
# C2 :  836
# Sending Ciphertext to the client
#
# Process finished with exit code 0
