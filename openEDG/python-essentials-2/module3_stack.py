class Stack0:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.stackList = []


s_object0 = Stack0()  # Instantiating the object.
print(len(s_object0.stackList))

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.__stackList = [] #Now it is private, cannot be accessed from outside

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


#s_object = Stack()  # Instantiating the object.
#print(len(s_object.__stackList))#will raise an exception 
stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
