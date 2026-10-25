# design of each node in linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        # if there is no element in linked list
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        else:
            newnode.next = self.head
            self.head = newnode

    def insert_at_last(self, data):
        newnode = Node(data)
        # if there is no elements in linked list
        if self.head == None:
            self.head = newnode
            return
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = newnode

    # printing all the linkedlist elements
    def display(self):
        if self.head == None:
            print("There is no element in linked list")
            return

        current_node = self.head
        while current_node != None:
            print(
                current_node.data,
                "-->",
                end="",
            )
            current_node = current_node.next
        print("end")

    # deleting the first elements
    def delete_first(self):
        if self.head == None:
            print("There is no elements in linkedlist")
            return

        # if there is single elements
        if self.head.next.next == None:
            self.head = None
            return

        self.head = self.head.next

    # deleting last elements
    def delete_last(self):
        if self.head == None:
            print("there is no elements in linkedlist")
            return

        # if there is single elements
        if self.head.next.next == None:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None

    # size of all elements
    def size_of_ll(self):
        if self.head == None:
            print("there is no elements in linkedlist")
            return
        count = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            count += 1
        print(count)


ll = SingleLL()
ll.display()

# insert the elements at first
ll.insert_at_first(10)
ll.insert_at_first(11)
ll.insert_at_first(13)


# insert the elements at last
ll.insert_at_last(100)
ll.insert_at_last(101)
ll.insert_at_last(102)
# display all the elements
ll.display()

# # delete the first elements
# ll.delete_first()
ll.size_of_ll()
ll.delete_last()
ll.display()
ll.size_of_ll()

#
