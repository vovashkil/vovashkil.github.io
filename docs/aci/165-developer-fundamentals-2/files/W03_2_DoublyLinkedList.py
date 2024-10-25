# Node objects wrap data and have 2 pointers: next & prev 
class Node:  
     def __init__(self, data): 
         self.item = data 
         self.next = None 
         self.prev = None 
 
# Doubly linked list (non-circular) 
class DoublyLL: 
    def __init__(self): 
         self.head = None 
         self.tail = None 
 
    # Add a node to the head of the list 
    def add_to_head(self, data): 
        new_node = Node(data) 
        old_head = self.head 
        new_node.next = old_head 
        if old_head is not None: 
             old_head.prev = new_node 
        self.head = new_node 
        if self.tail is None: 
            self.tail = new_node 
 
    # Add a node to the tail of the list  
    def add_to_tail(self, data):  
         new_node = Node(data)  
         old_tail = self.tail  
         new_node.prev = old_tail  
         if old_tail is not None:  
            old_tail.next = new_node 
         self.tail = new_node 
         if self.head is None: 
             self.head = new_node 
 
    # Demonstrate traversing forward 
    def print_list_forward(self): 
         current = self.head 
         while current is not None: 
             print(current.item) 
             current = current.next 
 
    # Demonstrate traversing backward 
    def print_list_backward(self): 
         current = self.tail 
         while current is not None: 
             print(current.item)  
             current = current.prev 
 
# Create a linked list object and add nodes to the tail of the list 
linked_list = DoublyLL() 
linked_list.add_to_tail('barcelona') 
linked_list.add_to_tail('real') 
linked_list.add_to_tail('atletico') 
 
# Print the list forward 
print("Printing the list forward (head to tail):") 
linked_list.print_list_forward() 
 
# Print the list backwards 
print("Printing the list backward (tail to head):") 
linked_list.print_list_backward() 
 
# Add nodes to the head of the list 
print("\nNow adding first, second, third to the HEAD of the list") 
linked_list.add_to_head('first@head') 
linked_list.add_to_head('second@head') 
linked_list.add_to_head('third@head') 
 
# Print the list forward 
print("Printing the list forward (head to tail):") 
linked_list.print_list_forward() 
 
# Print the backward 
print("Printing the list backward (tail to head):") 
linked_list.print_list_backward() 