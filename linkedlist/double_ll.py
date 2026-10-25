class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None 



class DDL:
    def __init__(self):
        self.head = None 

    def insert_at_first(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return 
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode 

    def insert_at_last(self,data):
        newnode= Node(data)
        if self.head == None:
            self.head = newnode
            return 
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next 

        newnode.prev = current_node
        current_node.next = newnode 


    def display(self):
        if self.head == None:
            print("There is no elements")
            return 
        current_node = self.head
        while current_node != None:
            print(current_node.data,"-->",end="")
            current_node = current_node.next 
        print("end")

# printing all the data into reverse order
    def print_reverse(self):
        if self.head == None:
            print("There is no elements")
            return 

        current_node= self.head
        while current_node.next != None:
            current_node = current_node.next 

        while current_node != None:
            print(current_node.data,"-->",end="")
            current_node = current_node.prev 
        print("end")


    def delete_first(self):
        if self.head == None:
            print("There is no elements in linkedlist")
            return 

        if self.head.next == None:
            self.head = None 
            return 

        self.head = self.head.next  

    def delete_last(self):
        if self.head == None:
            print("There is no elements in linkedlist")
            return 
        
        if self.head.next == None:
                self.head = None 
                return 

        current_node = self.head 
        while current_node != None:
            current_node = current_node.next 
        
        
        

dd = DDL()
dd.insert_at_first(10)
dd.insert_at_first(12)
dd.insert_at_first(13)
dd.display()
# dd.print_reverse()
dd.delete_first()
dd.display()



        