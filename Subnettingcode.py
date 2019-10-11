#THIS IS A TEST VERSION
#THIS VERSION GENERATES A RANDOM NETWORK, HOWEVER IT'S A /32 SUBNET, SO IT'S SINGLE ADDRESS
#PROOF OF CONCEPT


#Imports the necessary functions from libraries
from random import getrandbits
from ipaddress import IPv4Address
from ipaddress import IPv4Network

#Just for now
v = 4

if v == 4:
    bits = getrandbits(32)#generates an integer with 32 random bits
    address = IPv4Network(bits) # instances an IPv4Network object from those bits
    addr_str = str(address) # get the IPv4Address object's string representation

#Prints the network
print(addr_str)

#Asks the user for input
Address=str(input("Please input IPv4Address "))

#Checks if the address is the broadcast address:
if Address in addr_str:
    print("True")
else:
    print("False")
