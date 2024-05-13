# print("I like to be a module")
# print(__name__)
# if __name__ == "__main__":
#     print("name is main, so we have run the module file itself")
#     # I can run some useful function tests here
#     # they will be executed only if I run the module file itself
# else:
#     print("name is not main, so the module was imported")
""" myModule.py - an example of a python module"""

__counter = 0


def sumList(a_list):
    global __counter
    __counter += 1
    sum = 0
    for element in a_list:
        sum += element
    return sum

def productList(a_list):
    global __counter
    __counter += 1
    prod = 1
    for element in a_list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("I am not an imported module yet, let's do some tests:")
    lili = [i+1 for i in range(5)]
    print(sumList(lili) == 15)
    print(productList(lili) == 120)

