import math
# from math import* (not safe, imports all the functions sin())
# from math import sin (convenient, but can cause the conflict sin())
# import math as m ( then the ivocation will be: m.sin())
# from math import sin as SINE (invocation will be: SINE())

# sin from math and sin created here are not in conflict
# print(math.sin(math.pi/2))
# def sin(x):
#     print("This is handmade sin function")
# sin(1)
# print(dir(math))
# from platform import platform
# from platform import processor
# from platform import system

# print(platform())
# print(platform(1))
# print(platform(0, 1))
# print(processor())
# print(system())

import sys

for p in sys.path:
    print(p)



