"""
Your task is to implement the Queue class with two basic operations:

put(element), which puts an element at end of the queue;
get(), which takes an element from the front of the queue and returns it as the result 
(the queue cannot be empty to successfully perform it.)
"""

class QueueError(LookupError):  # Choose base class for the new exception.
    def __init__(self):
        LookupError.__init__(self)


class Queue:
    def __init__(self):
        self.__list = []

    def put(self, elem):
        self.__list.insert(0, elem)

    def get(self):
        try:
            element = self.__list[-1]
            del self.__list[-1]
            return element
        except:
            raise QueueError
        


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
