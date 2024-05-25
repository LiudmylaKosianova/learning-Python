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
        self.list = []

    def put(self, elem):
        self.list.insert(0, elem)

    def get(self):
        try:
            element = self.list[-1]
            del self.list[-1]
            return element
        except:
            raise QueueError
     
    #
    # Code from the previous lab.
    #


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        return self.list == []

    
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
