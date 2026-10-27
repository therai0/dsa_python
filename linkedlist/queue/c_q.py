""" 
Implementing the circular queue with array
"""

class Queue:
    def __init__(self,size):
        self.size = size 
        self.array = [int]*size 
        self.font = -1
        self.rear = -1

    def is_empty(self):
        return self.font == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.font 

    def enqueue(self,data):
        # check queue is full or not:
        if self.is_full():
            print("Queue is full")
            return 

        if self.is_empty():
            self.font = 0

        self.rear = (self.rear + 1) % self.size
        self.array[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return 
        value = self.array[self.font]
        self.array[self.font] = None 
        print(value)

        # check the queue is empty or not during the dequeue operation
        if self.rear == self.font:
            self.rear = -1
            self.font = -1
        else:
            self.font = (self.font + 1) % self.size

    def print_queue(self):
        if self.rear == -1:
            print("Queue is empty")
        i = self.font
        while True:
            print(self.array[i],"-->",end="")
            if i == self.rear:
                break 
            i = (i+1)% self.size
        print("end")

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print(self.array[self.font])

    
        

q = Queue(4)
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)

q.print_queue()
q.peek()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()