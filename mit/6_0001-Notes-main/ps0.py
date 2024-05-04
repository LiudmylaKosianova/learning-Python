#Raising a number to a power and taking a logarithm
import numpy as np

user_in = input("Enter number x: ")
try:
    intX = int (user_in)
except ValueError :
    print("Not a valid number")
    exit()
    
user_in = input("Enter number y: ")
try:
    intY = int (user_in)
except ValueError :
    print("Not a valid number")
    exit()
#powerX = intX**intY
print("x**y = ", intX**intY)
print("log(x) = ", int(np.log2(intX)))



