import sympy
import random
import socket

client = socket.socket()

# ip address and port of the server
IP_address = "127.0.0.1"
Port = 55555

# connecting to the server
client.connect((IP_address, Port)) 
print("\nConnected to Server\n")


print("Generating Keys...")
# Key generation
P = sympy.randprime(1000, 5000)
d = random.randint(1,P-2)
E1 = random.randint(2,1000)
E2 = (E1**d)%P
print("P : ",P)
print("d : ",d)
print("E1 : ",E1)
print("E2 : ",E2)

print("Sending Public Key to the Server...")
# sending P, E1 and E2
client.send(bytes(str(P),'utf-8'))
client.send(bytes(str(E1),'utf-8'))
client.send(bytes(str(E2),'utf-8'))
print("Receiving Ciphertext...")
# Getting C1
C1 = client.recv(2048)
if C1:
	C1 = int(C1.decode('utf-8'))

# Getting C2
C2 = client.recv(2048)
if C2:
	C2 = int(C2.decode('utf-8'))

print(f"Ciphertext Received {C1} and {C2}")
# decryption process
PT = (C2 * (C1 ** ((-d%P) -1) ) ) % P
print("Plain text Decrypted fron Ciphertext:",PT)

client.close()
# Connected to Server
#
# Generating Keys...
# P :  1597
# d :  1027
# E1 :  315
# E2 :  1586
# Sending Public Key to the Server...
# Receiving Ciphertext...
# Ciphertext Received 1565 and 836
# Plain text Decrypted fron Ciphertext: 100
#
# Process finished with exit code 0
