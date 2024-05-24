class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.stackList = []


s_object = Stack()  # Instantiating the object.
print(len(s_object.stackList))

class Stack2:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.__stackList = [] #Now it is private, cannot be accessed from outside


s_object2 = Stack2()  # Instantiating the object.
print(len(s_object.__stackList))
