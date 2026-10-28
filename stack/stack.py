

class Stack:
    def __init__(self,size:int):
        self.size = size
        self.arr = [None] * size 
        self.index = -1 

    def is_empty(self):
        return self.index == -1
    
    def is_full(self):
        return self.index == self.size-1

    def push(self,data):
        if self.is_full():
            print("Stackoverflow")
            return 
        self.index += 1 
        self.arr[self.index] = data 

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return 
        print(self.arr[self.index])
        self.index -= 1 

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return 
        for i in range(0,self.index+1):
            print(self.arr[i])

s = Stack(5)

# print(s.is_empty())
# s.pop()
s.push(10)
s.push(11)
s.push(12)
s.push(13)
s.push(14)

# s.display()
s.pop()
s.display()


    
