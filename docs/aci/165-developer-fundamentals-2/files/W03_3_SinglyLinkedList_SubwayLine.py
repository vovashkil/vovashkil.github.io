# Create node class  
class Node:   
    def __init__(self, data): 
        self.item = data 
        self.next = None 
        self.prev = None 
 
# Create a linked list class  
class LinkedList:   
    def __init__(self):   
        self.head = None 
        self.tail = None 
 
    # Add nodes 
    def add_to_head(self, data): 
        new_node = Node(data) 
        old_head = self.head 
        new_node.next = old_head 
        if old_head is not None: 
            old_head.prev = new_node 
        self.head = new_node 
        if self.tail is None: 
            self.tail = new_node 
 
    # Print the nodes 
    def print_list(self): 
        current = self.head 
        while current is not None: 
            print(current.item) 
            current = current.next 
 
# Create a linked list object
 
subway_line = LinkedList()
 
# Add the nodes and data 
subway_line.add_to_head('Red Station')
subway_line.add_to_head('Green Street')
subway_line.add_to_head('Blue Square')

# Print the linked list 
subway_line.print_list()
