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
        while current_node.next.next != None:
            current_node = current_node.next

        current_node.next = None

    def get_size(self):
        if self.head == None:
            print("No elements in linked list")
            return 0
        count = 0
        current_node = self.head
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count

    def get_nth_node(self,n:int):
        if self.head == None:
            print("There is no elements in linkedlist")
            return
        
        size = self.get_size()
        if size < n:
            print("Large index")
            return 

        current_node = self.head
        while n > 0:
            current_node = current_node.next
            n -= 1
        print(current_node.data)

    
    def delete_nth_node(self,n:int):
        if self.head == None:
            print("There is no elements in linkedlist")
            return
        size = self.get_size()
        if (size-1) < n:
            print("Large index")
            return 
        # explicitly handling the case if index is 0
        if n == 0:
            self.head = self.head.next
            return 
        
        current_node = self.head 
        while (n-1) > 0:
            current_node = current_node.next
            n -= 1
        current_node.next = current_node.next.next 

        

        
        
        

dd = DDL()
dd.insert_at_first(10)
dd.insert_at_first(11)
dd.insert_at_first(12)
dd.insert_at_first(13)
dd.insert_at_first(14)
dd.display()
# dd.print_reverse()
# dd.delete_first()
# dd.delete_last()

# delete the nth node
dd.delete_nth_node(0)
dd.delete_nth_node(0)

# dd.get_nth_node(0)
# dd.get_nth_node(1)
# dd.get_nth_node(2)

dd.display()



        