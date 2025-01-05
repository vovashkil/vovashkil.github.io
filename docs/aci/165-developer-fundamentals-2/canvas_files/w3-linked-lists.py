#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Linked Lists
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# A **linked list** is a data structure that stores data as a **collection of nodes**. Each node contains:
# - The **data** we are storing
# - A **pointer** to the next node

# ## Quick Refresher on Time Complexity
# Just a quick **reminder** that **time complexity**, which **measures** our **time efficiency**, is all about **how many times** we **repeat steps**.
# - If we have a **fixed steps** that do **not repeat based on the input**, we call that **"Constant Time"** time, or **O(1)**, and that's the **most efficient**.
# - If we have to **repeat steps "n" times**, where **"n"** is something that **can change based on the input** (**like** the **size of** a **list**), we call that **"Linear Time"**, or **O(n)**, and that's **not too bad**, but **less efficient than O(1)**, particularly **if "n"** is very **large**.
# - There are **many others** (O(log(n), O(n<sup>2</sup>), etc), and it always **depends** on **how many times** you are **repeating operations**.
# 
# These are **topics we will study in depth in later modules**, but it's **good to start thinking** about that as we study operations. Start thinking:
# - *"This operation returned with only a few fixed steps. That will be very fast"*
# - *"Hum ... this operation requires me to walk through a whole list. That can be slower if the list is very long.*

# # Bare bones Linked List
# The "classic" linked list is a **singly linked list**, which is **traversed** only **forward**. Each **node has** a **pointer to** the **next node**.

# ## Node Class

# In[ ]:


class Node:
    '''
    Node for a singly linked list
    '''
    def __init__(self, data):
        '''
        Parameters:
            data: The data to be stored in the node
            next: Pointer to the next node
        '''
        self.data = data
        self.next = None


# ## LinkedList Class
# A very **basic linked list** needs **nothing more than** initializing a **head pointer**. The **rest** is all about **how we manipulate the nodes**.

# In[ ]:


class LinkedList:
    '''
    A basic linked list
    '''
    def __init__(self):
        # initialize the head of the list
        self.head = None


# How does something so simple implement a list? It's all about how you **manipulate** the **nodes and pointers**.

# ## Linked List Operations
# Operating a linked list is all about manipulating the pointers in the nodes. We'll see this below.

# ### Creating a linked list
# **Creating** my **simple linked list** will simply **create an empty head pointer**. The head will initially be pointing to None.

# In[ ]:


my_ll = LinkedList()


# ### Inserting a new item to the beginning of the list
# **Inserting** an item **to** the **beginning** is fast, because you only need to **adjust** the **head pointer and** the **new node**.

# In[ ]:


# create a node with data "Tucker"
new_node = Node("Tucker")

# point the next pointer of the new node to the current head of the list
new_node.next = my_ll.head

# now update the list head to point to the new node
my_ll.head = new_node


# The **same** simple **process** can be **used every time** we **insert at the beginning**.

# In[ ]:


# create a node with the data "Finn"
new_node = Node("Finn")

# point the new node next pointer to the current head of the list
new_node.next = my_ll.head

# now update the list head to point to the new node
my_ll.head = new_node


# **Note** that **however long** my **list may be**, to insert in the beginning, I **only had to manipulate two nodes**: the new node and the current head. So **inserting in the beginning** is **very fast** on a singlly linked list.

# ### Traversing a linked list
# **To traverse** the linked list, you **start at the head**, than **use** the **next pointer** in each node **to "hop" to the next one**.
# 
# As an **example**, let's create a **function to traverse a list** and **print every element**.

# In[ ]:


def print_list(list):
    # traverse through the linked list and print each item
    node = list.head
    while node:
        print(node.data, end="")

        # If there is another item, print a separator, else just print new line
        if node.next:
            print(" --> ", end="")
        else:
            print()

        # update node pointer to the next node
        node = node.next


# Let's **try** our **traversal and print**, and see what our current list looks like.

# In[ ]:


# print current list
print_list(my_ll)


# ### Adding a new item to the end of the list
# **Adding** an item **to** the **end** is not hard, but it **requires** that you **traverse the whole list** to reach the end.

# In[ ]:


# create a node with the data "Moose"
new_node = Node("Moose")

# start at the head
node = my_ll.head

# traverse the list until we find the last node
while node.next:
    node = node.next

# now "node" is the last node, so we point it to the new node
node.next = new_node

# print current list
print_list(my_ll)


# **Although functionally** it **may sound like inserting** at the **beginning or** the **end makes no difference**, we can see that **adding it to the end** will requiring **traversing all** the **nodes**. For a large list, that can make a **sitgnificant performance difference**.

# ### Getting the first element in the list
# **Getting** the **first** element is very easy. You just **refer to the head**. So again, that will **only impact one node**.

# In[ ]:


# get the first element (check for empty list)
print(f"First element: {my_ll.head.data}")


# ### Getting the last of the list
# **Getting** the last element will **require traversing** the **list** till the end. Not as effective as getting the first element.

# In[ ]:


# traverse the list until we find the last node
node = my_ll.head
while node.next:
    node = node.next

# now "node" is the last node, so we set the dat from it
print(f"Last element: {node.data}")


# ### Removing an item in the middle of the list
# **Removing** an **item** from the list is again all about **manipulating the pointers**. We'll write a function that can traverse a list, and delete an item matching a value. We will have to **adjust** the **pointer** for the **item before the one being deleted**, so we'll need keep track of the previous item as we traverse the list.

# In[ ]:


def delete_item(list, search_val):
    # check for an empty list
    if (list.head is None):
        print("Empty list")
        return
        
    # if the item at the head is the one we need ...
    if (list.head.data == search_val):
        # simply adjust head to be the 2nd item
        list.head = list.head.next
        return

    # keep track of the previous node
    prev_node = list.head
    # move the search node ahead (since we already checked the head)
    node = list.head.next
    
    # traverse through the linked list looking for the search string
    while node:
        # if the current item is the one we need ...
        if (node.data == search_val):
            # redirect the previous node next pointer, to the current node next, which will skip the current item
            prev_node.next = node.next
            return
    
        # update the previous node, and move the search node ahead
        prev_node = node
        node = node.next


# Althout this **may look complicated** from a **code perspective**, note that **when** we **identified** the **item to delete**, we **only needed to manipulate the immediate items around it**. There was no need to impact any other items. That's **not the case in other data structures**. In an array for instance, since you cannot have an empty index, removing an item in the middle requires you to move back all the items after it to close that gap.

# Let's try out our function.

# In[ ]:


# print the current list
print("Current list: ", end="")
print_list(my_ll)

# delete the "Tucker" item
print("\nDeleting an item ...\n")
delete_item(my_ll, "Tucker")

# print the updated list after delete
print("Updated list: ", end="")
print_list(my_ll)


# # Full Featured Singly Linked List
# To create a full featured singly linked list, we just **add** the **code** implementing the operations we wrote earlier **into a class**

# ## SinglyLL Class

# In[ ]:


class SinglyLL:
    '''
    A singly linked list
    '''
    def __init__(self):
        # initialize the head of the list
        self.head = None

    def insert(self, data):
        '''
        Insert an item at the beginning of the list

        Parameters:
            data: The data to be stored in the new node
        '''
        # create a new node with the data
        new_node = Node(data)
        # point the new node next pointer to the current head
        new_node.next = self.head
        # update the head pointer to point to the new node
        self.head = new_node

    def append(self, data):
        '''
        Insert an item at the end of the list

        Parameters:
            data: The data to be stored in the new node
        '''
        # create a new node with the data
        new_node = Node(data)

        # traverse the list until we find the last node
        node = self.head
        while node.next:
            node = node.next

        # now "node" is the last node, so we point it to thw new node
        node.next = new_node

    def get_first(self):
        '''
        Returns the first element in the list
        '''
        if (self.head):
            return self.head.data
        else:
            return None

    def get_last(self):
        '''
        Returns the last element in the list
        '''
        if (self.head is None):
            return None
            
        # traverse the list until we find the last node
        node = self.head
        while node.next:
            node = node.next
        
        # now "node" is the last node, so we get the data from it
        return node.data

    def get_all(self):
        '''
        Returns a list with all the values in order
        '''
        return_list = []
            
        # traverse the list until the end, and append each item
        node = self.head
        while node:
            return_list.append(node.data)
            node = node.next
        
        # return the list
        return return_list
            
    def delete_item(self, search_val):
        
        if (self.head is None):
            print("Empty list")
            return
            
        # if the item at the head is the one we need ...
        if (self.head.data == search_val):
            # simply adjust head to be the 2nd item
            self.head = self.head.next
            return
    
        # keep track of the previous node
        prev_node = self.head
        # move the search node ahead (since we already checked the head)
        node = self.head.next
        
        # traverse through the linked list looking for the search string
        while node:
            # if the current item is the one we need ...
            if (node.data == search_val):
                # redirect the previous node next pointer, to the current node next, which will skip the current item
                prev_node.next = node.next
                return
        
            # update the previous node, and move the search node ahead
            prev_node = node
            node = node.next
        
    def __str__(self):
        # initialize string
        pr_str = ""

        # traverse through the linked list and append each item
        node = self.head
        while node:
            pr_str += node.data
    
            # If there is another item, print a separator
            if node.next:
                pr_str += " --> "
    
            # update node pointer to the next node
            node = node.next

        # return string constructed
        return pr_str


# ## Repeat operations on the new class
# Now we can do all the same operations with simple calls to the new class

# In[ ]:


# create a new linked list
my_ll = SinglyLL()
print("\nCreating list, and adding four elements ...\n")

# add data to the beginning of the list
my_ll.insert("Tucker")
my_ll.insert("Finn")

# add a few more items to the end of the list
my_ll.append("Lexi")
my_ll.append("Moose")

# print current list
print(f"Current list: {my_ll}")

# print first and last elements
print(f"\nFirst element: {my_ll.get_first()}\nLast element: {my_ll.get_last()}")


# In[ ]:


# delete item in the middle
print("\nDeleting Lexi ...\n")
my_ll.delete_item("Lexi")

# print updated list
print(f"Updated list: {my_ll}")


# In[ ]:


# delete first item
print("\nDeleting Finn ...\n")
my_ll.delete_item("Finn")

# print updated list
print(f"Updated list: {my_ll}")


# # Doubly Linked List
# A **double linked list** will follow the **same principles**, but will simply have **pointers in both directions**. So not only we have a *head* and *next* **pointers**, but we **also** have a ***tail*** and ***prev*** **pointers**.

# **Maintaining** these **extra pointers** takes **more space**, **but** it will make **some operations** much **more efficient**. 

# ## Node Class
# The Node class for a doubly linked list is similar, but **needs** the extra ***prev* pointer**

# In[ ]:


class Node:
    '''
    Node for a singly linked list
    '''
    def __init__(self, data):
        '''
        Parameters:
            data: The data to be stored in the node
            next: Pointer to the next node
            prev: Pointer to the previous node
        '''
        self.data = data
        self.next = None
        self.prev = None


# ## DoublyLL Class
# Pay close attention to the ***append*** and ***get_last*** operations, to see how **more efficient** they are with **no need** to **traverse** the **whole list**.

# In[ ]:


class DoublyLL:
    '''
    A singly linked list
    '''
    def __init__(self):
        # initialize the head of the list
        self.head = None
        self.tail = None

    def insert(self, data):
        '''
        Insert an item at the beginning of the list

        Parameters:
            data: The data to be stored in the new node
        '''
        # create a new node with the data
        new_node = Node(data)

        # if the list was empty, just set head and tail to new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
            
        # point the new node next pointer to the current head
        new_node.next = self.head
        # update the current head node to point back to the new node
        self.head.prev = new_node
        # update the head pointer to point to the new node
        self.head = new_node


    def append(self, data):
        '''
        Insert an item at the end of the list

        Parameters:
            data: The data to be stored in the new node
        '''
        # create a new node with the data
        new_node = Node(data)

        # if the list was empty, just set head and tail to new node
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
            
        # point the new node prev pointer to the current tail
        new_node.prev = self.tail
        # update the current tail node to point forward to the new node
        self.tail.next = new_node
        # update the tail pointer to point to the new node
        self.tail = new_node


    def get_first(self):
        '''
        Returns the first element in the list
        '''
        if (self.head):
            return self.head.data
        else:
            return None

    def get_last(self):
        '''
        Returns the last element in the list
        '''
        if (self.tail):
            return self.tail.data
        else:
            return None

    def get_all(self):
        '''
        Returns a list with all the node values in order
        '''
        return_list = []
            
        # traverse the list until the end, and append each item
        node = self.head
        while node:
            return_list.append(node.data)
            node = node.next
        
        # return the list
        return return_list
            
    def delete_item(self, search_val):
        '''
        Delete an item from the list

        Parameters:
            search_val: value to delete
        '''
        # check for an empty list
        if (self.head is None):
            print("Empty list")
            return
            
        # traverse through the linked list till the end or until target item is found
        target_node = None
        node = self.head
        while node and (not target_node):
            # if the current item is the one we need ...
            if (node.data == search_val):
                # redirect the previous node next pointer, to the current node next, which will skip the current item
                target_node = node
            # update node to the next one
            node = node.next

        # if node was not found do nothing
        if (not target_node):
            return

        # if there was only one item ...
        if self.head == self.tail:
            # set both head and tail to None
            self.head = None
            self.tail = None
        
        # if target_node was the head ...
        elif (target_node == self.head):
            # adjust head to be the next item after
            self.head = target_node.next
            # reset the new heard item previous to None
            self.head.prev = None

        # if target_node was the tail ...
        elif (target_node == self.tail):
            # adjust tail to be the previous item
            self.tail = target_node.prev
            # reset the new tail item previous to None
            self.tail.next = None
            return
        # else, redirect previos and next pointer on the item before and after
        else:
            # redirect the previous node next pointer, to the current node next, which will skip the target item
            target_node.prev.next = target_node.next
            # redirect the next node prev pointer, to the current node prev, which will skip the target item
            target_node.next.prev = target_node.prev
        
    def __str__(self):
        # initialize string
        pr_str = ""

        # traverse through the linked list and append each item
        node = self.head
        while node:
            pr_str += node.data
    
            # If there is another item, print a separator
            if node.next:
                pr_str += " <--> "
    
            # update node pointer to the next node
            node = node.next

        # return string constructed
        return pr_str


# ## Repeat operations on the new class
# Now we can do all the same operations with simple calls to the new class

# In[ ]:


# create a new linked list
my_ll = DoublyLL()
print("\nCreating list, and adding four elements ...\n")

# add data to the beginning of the list
my_ll.insert("Tucker")
my_ll.insert("Finn")

# add a few more items to the end of the list
my_ll.append("Lexi")
my_ll.append("Moose")

# print current list
print(f"Current list: {my_ll}")


# In[ ]:


# delete item in the middle
print("\nDeleting Lexi ...\n")
my_ll.delete_item("Lexi")

# print updated list
print(f"Updated list: {my_ll}")


# In[ ]:


# delete first item
print("\nDeleting Finn ...\n")
my_ll.delete_item("Finn")

# print updated list
print(f"Updated list: {my_ll}")


# # <span style="color:blue"> OPTIONAL

# We discussed stacks earlier. Let's **implement** a **stack** using our own **DoublyLL class**. At a minimum, we will need to **implement** a *push()* and a *pop()*.

# ### MyStack Class

# In[ ]:


class MyStack:
    '''
    A stack implemented using a Doubly Linked List. We'll consider the beginning of the list as the top, and the
    end of the list as the bottom.
    '''
    def __init__(self):
        self.stack_list = DoublyLL()

    def push(self, item):
        '''
        Push an item onto the stack, by adding it to the begginning.

        Parameters:
            item: The item to be pushed onto the stack
        '''
        self.stack_list.insert(item)

    def pop(self):
        '''
        Pop an item from the stack, by retrieving it from the beginning, and removing it.

        Returns:
            The item popped from the stack, or None if the stack is empty
        '''
        # retrieve first item
        item = self.stack_list.get_first()
        # delete first item
        self.stack_list.delete_item(item)
        # return item
        return item

    def __str__(self):
        # get all the notes in the list
        node_list = self.stack_list.get_all()
        
        output = "[TOP]\n"
        for item in node_list:
            output += f"{item}\n"
        output += "[BOTTOM]"
        return output


# #### Perform stack operations

# In[ ]:


# Create a stack
my_stack = MyStack()

# push some items to the stack
print(f"\nPushing 3 items to the stack ...")
my_stack.push("Tucker")
my_stack.push("Finn")
my_stack.push("Lexi")

# print the stack
print(f"\nStack:\n{my_stack}")

# pop the top item in the stack
print(f"\nPop item: {my_stack.pop()}")

# print the stack
print(f"\nStack now is:\n{my_stack}")

# push another item to the stack
print(f"\nPushing Moose to stack ...")
my_stack.push("Moose")

# print the stack
print(f"\nStack now is:\n{my_stack}")


# In[ ]:




