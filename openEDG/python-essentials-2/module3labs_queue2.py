"""
Scenario
Your task is to slightly extend the Queue class' capabilities. 
We want it to have a parameterless method that returns 
True if the queue is empty and False otherwise.
"""

class QueueError(IndexError):
    pass


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
    def get_list(self):
        return self.__list
    #
    # Code from the previous lab.
    #


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        return self.get_list == []

    
    #
    # Write new code here.
    #


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
