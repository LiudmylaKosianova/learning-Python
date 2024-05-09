# """
# Functions
# """
# print("\n*** Function. Arguments ***\n")
# def fruits(nApples, nPlums, nCherries):
#     print("We have", nApples, "apples")
#     print("We have", nPlums, "plums")
#     print("We have", nCherries, "cherries")

# fruits(2, 5, 7) #positional arguments
# fruits(nCherries=2, nApples=5, nPlums=7) #keyword arguments
# fruits(2, nCherries=0, nPlums=7) #mix positional and keyword.Positional should go first

# def colours(cOne, cTwo="red"): #pre-defined argument
#     print("Colour one is:", cOne)
#     print("Colour two is:", cTwo)

# colours("blue")
# colours("blue", "pink")

# print("\n*** Function. Return ***\n")
# 
def oddFunction(n): # when the even number passed, it will return None
    if n%2 != 0:
        return True
    
print(oddFunction(9))
print(oddFunction(10))

def listFunction(n):
    print(len(n))

listFunction([1,2,77])

# interesting use of "\"

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
       weight < 20  or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

isItOrdered = {1:"red", 2:"pink", 3:"white", 4:"black"}
print(isItOrdered)
