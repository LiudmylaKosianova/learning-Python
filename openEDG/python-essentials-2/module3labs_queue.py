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
