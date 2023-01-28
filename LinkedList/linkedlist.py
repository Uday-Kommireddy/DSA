class Node:
    def __init__(self, value):
        self.data = value 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    """
    Inserting a new Node in LinkedList
    If head is None, newly inserting node will be Head,
    Else iterate through the linkedlist, find the last node, and insert new node
    """
    def insert_into_linkedlist(self,  value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node 
        
        else:
            current_node = self.head 
            while current_node.next is not None:
                current_node = current_node.next 
            
            current_node.next = new_node 

    """
    Inserting a new node at head of linked list.
    If head is None this will be new Node,
    Else store the existing head in temprary variable, assign the node as new head, and head's next to temporary 
    """
    def insert_node_at_head(self, value):
        new_node = LinkedList(value)

        if not self.is_not_none():
            self.head = new_node
        
        else:
            temp = self.head 
            self.head = new_node
            self.head.next = temp 

    """
    Length of LinkedList.
    Iterate through the LinkedList, increament count
    """
    def length_of_linked_list(self):
        count = 0

        if self.head == None:
            return count
        else:
            current_node = self.head 
            while current_node:
                count += 1
                current_node = current_node.next 

        return count

    """
    Checking if LinkedList is not None
    """
    def is_not_none(self):
        return True if self.head is not None else False 

    """
    Deleting a node from LinkedList
    In linkedlist, for deletion we will be traversing through out the linkedlist, 
    If linkedlist node's value is equals to Value the that needed to be deleted. 
    If found, cuurent_node's next will be current_node next's next
    """
    def delete_from_linked_list(self, value):
        if not self.is_not_none():
            print('Deletion Error: The list is empty.')
            return 

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current:
            if current.data == value:
                break
            previous = current
            current = current.next

        # If the key was not found
        if current is None:
            print('Deletion Error: Key not found.') 
        else:
            previous.next = current.next
            
    """
    Displaying LinkedList
    """
    def display(self):
        if self.is_not_none():
            current_node = self.head 
            while current_node:
                print(str(current_node.data) + " ->", end=" ")
                current_node = current_node.next 
            print("Null")


ll = LinkedList()
ll.insert_into_linkedlist(1)
ll.insert_into_linkedlist(3)
ll.display()
ll.delete_from_linked_list(3)
ll.display()
ll.delete_from_linked_list(1)
ll.display()
print(ll.is_not_none())