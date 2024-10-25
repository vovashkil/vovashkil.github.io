#!/usr/bin/env python3

# Create Node class  
class Node:   
    def __init__(self, data): 
        self.item = data 
        self.pointer = None 
 
# Create a singly linked list class 
class SinglyLL:   
    def __init__(self):   
        self.head = None   
  
    # Add nodes 
    def add_to_head(self, data): 
        new_node = Node(data)  
        new_node.pointer = self.head 
        self.head = new_node       
 
    # Print the list 
    def print_list(self): 
        temp = self.head 
        while temp is not None: 
            print(temp.item) 
            temp = temp.pointer 
  
# Create a linked list object and add nodes 
linked_list = SinglyLL() 
linked_list.add_to_head('people') 
linked_list.add_to_head('the') 
linked_list.add_to_head('we') 
  
# Print the linked list 
linked_list.print_list() 