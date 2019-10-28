#Imports the necessary functions from libraries
import random
import ipaddress
from ipaddress import IPv4Network

winconIP = 0

SubList = ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
#Just for now
ip = ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(4))))
#IPfirst = IPv4Address(ip) #Marks the random IP as an IP address
subnet = ip + "/" + random.choice(SubList)
Network = IPv4Network(subnet, False) #Adds the IP to a subnet mask

#Prints the network
print(Network)
#print(Network.broadcast_address) #prints the broadcast address for the network, here for testing purposes

#Asks the user for input
Broadcast=str(input("Please input the broadcast address for the network "))

#Checks if the address is the broadcast address:
if Broadcast == str(Network.broadcast_address):
    print("Good job!")
    winconIP = 1
#    print(winconIP)
else:
    print("Wrong!")