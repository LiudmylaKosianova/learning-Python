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

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def get_sum(self):
        return self.__sum
    
print("***AddingStack***")
    
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
