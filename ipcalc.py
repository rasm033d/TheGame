import random
import ipaddress

ip = ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(4))))
network = str(ip + "/24")
print(network)

broadcast = str(input("Enter the host IP ")