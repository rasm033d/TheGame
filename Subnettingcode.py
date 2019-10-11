from random import getrandbits
from ipaddress import IPv4Address

v = 4

if v == 4:
    bits = getrandbits(32) # generates an integer with 32 random bits
    addr = IPv4Address(bits) # instances an IPv4Address object from those bits
    addr_str = str(addr) # get the IPv4Address object's string representation

print(addr_str)
