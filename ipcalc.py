#Imports the necessary functions from libraries
import random
import ipaddress
from ipaddress import IPv4Network
#List of subnets, in the way of /X
SubList = ["14", "15", "16", "17", "18", "19", "20"]
#Generates a random string of 4x 0-255
ip = ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(4))))
#Assings a subnet to the generated IP
subnet = ip + "/" + random.choice(SubList)
#Marks the IP and subnet as a network
Network = IPv4Network(subnet, False)

#Prints the network
print(Network)
