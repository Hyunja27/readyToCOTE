# You need to calculate how many hosts are possible to be in a IPv4 network.

# In a network (e.g.: 192.168.0.0/24) you can use all address except the first (192.168.0.0 -> network address) and last (192.168.0.255 -> broadcast address). So there are 254 addresses left to address a host (192.168.0.1 - 192.168.0.254).

# In a network with a subnetmask of X are Y addresses possible.

# X |Y
# 1 |2147483648
# ...
# 24 |256
# 25 |128
# ...
# 30 |4

# How to?:
# You must take the second part of the IPv4 Address, (92.168.0.0/24) and you must first find the absolute difference between it and 32, then you must compute 2 to the power of the number and then, subtract two from the result

from typing import MappingView


============

# # mine
# import sys
# import math

# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.

# input_count = int(input())
# for i in range(input_count):
#     ipaddress = input()

# # Write an answer using print
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)

# result = 32 - int(ipaddress[-2:])

# # print(input_count)
# # print(ipaddress)
# print(pow(2,result) - 2)

==========

# answer

# for i in range(int(input())):
#     ip=input()
#     if ip[len(ip)-2]=='/': ip = ip[len(ip)-1]
#     else: ip=ip[-2:]
#     w=int(ip)
#     #print(w)
#     print(2**(32-w)-2)