""" 
Implementing the queue with array
"""

class Queue:
    def __init__(self,size):
        self.array = [int]*size 
        self.size = size
        self.font = 0
        self.rear = 0

    def get_size(self):
        print(self.size)
        return

    def enqueue(self,data:int):
        # check if queue is full or not
        if self.rear == self.size:
            print("Queue is full")
            return
        self.array.insert(self.rear,data)
        self.rear +=1

    def dequeue(self):
        if self.rear == 0:
            print("Queue is empty")
            return
        print(self.array[self.font])
        self.font += 1

    def peak(self):
        if self.rear == 0:
            print("Queue is empty")
            return 
        print(self.array[self.font])
        
    def print_queue(self):
        if self.rear == 0:
            print("Queue is empty")
            return
        for x in range(self.font,self.rear):
            print(self.array[x],"--> ",end="")
        print("end")

q = Queue(5)
# q.print_queue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)
q.print_queue()
q.peak()
q.dequeue()
q.print_queue()
q.peak()