class RedSofa:
    pass

mySofa = RedSofa()

#stack precedural approach
stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
"""
instance variables
"""
# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val

#     def set_second(self, val):
#         self.second = val


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)

# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val

#     def set_second(self, val = 2):
#         self.__second = val


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)

# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.__third = 5


# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

"""
class variables
"""

# class ExampleClass:
#     __counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)

# print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
# print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
# print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

"""
__dict__
"""
# class ExampleClass:
#     varia = 1
#     def __init__(self, val):
#         ExampleClass.varia = val

# print("***")
# print(ExampleClass.__dict__)
# example_object = ExampleClass(2)
# print("*")
# print(ExampleClass.__dict__)
# print("*")
# print(example_object.__dict__)

"""
check if instance has an attribute
"""

class ExampleClass:
    redSofa = 99
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)
print(hasattr(ExampleClass, "redSofa"))

"""
class methods
"""
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()

class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

"""
As you know, any module named __main__ is actually not a module, 
but the file currently being run.
"""

class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)


"""
__dict__ is a dictionary. 

Another built-in property worth mentioning is __name__, which is a string.

The property contains the name of the class. It's nothing exciting, just a string.
Note: the __name__ attribute is absent from the object - it exists only inside classes.
"""

class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

"""
__bases__ is a tuple. T
he tuple contains classes (not class names) which are direct superclasses for the class.

The order is the same as that used inside the class definition.

Note: a class without explicit superclasses points to object (a predefined Python class) 
as its direct ancestor.
"""
class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

"""
introspection, which is the ability of a program to examine the type or properties of an object at runtime;
reflection, which goes a step further, and is the ability of a program to manipulate the values, properties and/or functions of an object at runtime.
"""


