#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Stacks and Queues
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Stacks in Python

# There are **multiple ways** that you can **implement stacks in Python**. Some of them were already covered in the eLearning. We'll give some examples here (some are in the eLearning, and some are not).

# ## Implementation #1: Using the built-in Python List as is
# The **standard Python List** class already has all the methods you need to implement a stack. It even **has a built-in** ***pop()*** method! As long as remember that the ***append()* method will be equivalent to a "push"**, because it adds an element at the end of the list, then you're done. When looking at the list, you need to **think of the end of the list as the top, and the first element as the bottom.**

# #### Creating my stack list

# In[ ]:


# Create a list to implement a stack. Having "stack" somewhere in the variable will remind me I want to use it as a stack
my_plain_stack = []


# #### Push elements to the stack using append()

# In[ ]:


# push a few items with append
my_plain_stack.append("First Item")
my_plain_stack.append("Second Item")
my_plain_stack.append("Third Item")
my_plain_stack.append("Fourth Item")


# #### Check my stack
# We can print the list to view the stack. Again, we have to **visualize** the **beginning as the bottom**, and the **end as the top**.

# In[ ]:


print(my_plain_stack)


# #### Pop top element from the stack
# We pop using the **standard *pop()* method** in List, which **also returns the element** that was popped.

# In[ ]:


# pop the top element from the stack
top_element = my_plain_stack.pop()
print(f'I just popped "{top_element}" from the stack')

# print the stack to confirm element is gone
print(f"Now the stack is: {my_plain_stack}")


# Let's do a few more (if we don't need the value popped, we don't need to assign it to a variable) ...

# In[ ]:


# pop two items
my_plain_stack.pop()
my_plain_stack.pop()

# push (append) a new item
my_plain_stack.append("New second item")

# check the stack
print(f"Now the stack is: {my_plain_stack}")


# ### Error handling, or lack thereoff
# So **what** happens **if** I try to **pop more items than I have?**

# In[ ]:


# pop three items, but I only have two
print(my_plain_stack.pop())
print(my_plain_stack.pop())

# this one will ... BOOM!
print(my_plain_stack.pop())


# ## Implementation #2: Custom stack class based on built-in List
# If we want to have **more robust error handling**, and implement some **additional friendly methods**, we can still **use** the **built-in List class**, but **wrap it around a class**. The MyStack below adds the following "enhancements":
# - A **"legit" *push()*** method
# - ***pop()*** method **preventing exception**
# - Added **friendly methods** like *peek()*, *length()*, and *is_empty()*
# - Added a ***print_stack()*** method that prints the stack so it **looks like a top to bottom stack**, with indicators

# In[ ]:


class MyStack:
    '''
    This class implements a standard Stack data structure using a Python built-in list class
    '''
    
    def __init__(self):
        '''
        Initialize the stack as an empty list
        '''
        self.list = []

    def push(self, item):
        '''
        Push an item onto the stack using the standard append method
        '''
        self.list.append(item)

    def pop(self):
        '''
        Pop the top item from the stack, or None if the stack is empty
        '''
        if self.is_empty():
            return None
        else:
            return self.list.pop()

    def peek(self):
        '''
        Return the top item from the stack without popping it, or None if the stack is empty
        '''
        if self.is_empty():
            return None
        else:
            return self.list[-1]

    def is_empty(self):
        '''
        Return True if stack is empty, or False if note
        '''
        return (len(self.list) == 0)
        
    def length(self):  
        '''
        Return the number of items in the stack
        '''
        return len(self.list)

    def print_stack(self):
        '''
        Print the stack like a stack, with items stacked top to bottom. The output will also have indicators for Top and Bottom
        '''
        # check for empty stack
        if (self.is_empty()):
            print("Stack is empty")
            return
        
        # print list items in reverse order, with a line break in between, so that last element is on top
        for n in reversed(range(len(self.list))):
            item = self.list[n]
            
            # if this is the first/bottom item, print an indicator for it
            if (n == 0):
                print("Bottom --> ".rjust(11), end = "")
            # else, pad the left with enough spaces to align, ehtn print item
            else:
                print("".rjust(11), end = "")

            # now print the item
            print(item, end = "")

            # if this is the last/top item, print an indicator for it
            if (n == len(self.list) - 1):
                print(" <-- Top")
            # else, just print a line break
            else:
                print()


# #### Creating my fancy stack object 

# In[ ]:


my_fancy_stack = MyStack()


# #### Push items into the stack, using our "legit" *push* method

# In[ ]:


# push a few items
my_fancy_stack.push("First Item")
my_fancy_stack.push("Second Item")
my_fancy_stack.push("Third Item")
my_fancy_stack.push("Fourth Item")


# #### Check my stack using my fancy *print_stack()*

# In[ ]:


my_fancy_stack.print_stack()


# Ooohhhh ... **how cool was that?!**

# #### Pop the top item, and check again

# In[ ]:


# pop the top element from the stack
top_element = my_fancy_stack.pop()
print(f'I just popped "{top_element}" from the stack')

# print the stack to confirm element is gone
print("\nStack now is:")
my_fancy_stack.print_stack()


# #### Try to break this one by popping more items than the stack has

# In[ ]:


print(my_fancy_stack.pop())
print(my_fancy_stack.pop())
print(my_fancy_stack.pop())
print(my_fancy_stack.pop())
print(my_fancy_stack.pop())
print(my_fancy_stack.pop())


# ## Implementation #3: Using the Collections module
# The **Collections module** (https://docs.python.org/3/library/collections.html) provides a number of **specialized data structure classes**. One such class is **Deque** (**pronounced "deck"**), which stands for ***"double ended queue"***, and we can use it to implement a stack or a queue. Deque offers a few useful features:
# - Uses **less memory** than the built-in list
# - **Items** can be **retrieved from either end** very efficiently
# 
# **Like** the **List** class, **deque has** a ***pop()*** method, and it has an ***append()*** we can use in liu of push. In fact it **also has** ***appendleft()*** and ***popleft()*** if we want to consider the left side as "top of the stack". It makes no difference, as long as we used it consistently.
# 
# In my **example** I'll **use append()/pop() to emphasize** it is very much **like using a regular list**. In fact I'll use nearly the same steps I did for List.

# #### Import collections.deque
# As usual, we need to import the module to use it.

# In[ ]:


from collections import deque


# #### Creating my stack deque 

# In[ ]:


# Create a new stack using deque   
my_dq_stack = deque()


# #### Push elements to the stack using append()

# In[ ]:


# push a few items with append
my_dq_stack.append("First Item")
my_dq_stack.append("Second Item")
my_dq_stack.append("Third Item")
my_dq_stack.append("Fourth Item")


# #### Check my stack
# We can **print** the **deque** to view the stack. Just like with the list, since we're appending to the end of the deque, we have to **visualize** the **beginning** as the **bottom of the stack**, and the **end as the top**.

# In[ ]:


print(my_dq_stack)


# #### Pop top element from the stack
# We pop using the **standard *pop()* method** in deque, which **also returns the element** that was popped.

# In[ ]:


# pop the top element from the stack
top_element = my_dq_stack.pop()
print(f'I just popped "{top_element}" from the stack')

# print the stack to confirm element is gone
print(f"Now the stack is: {my_dq_stack}")


# Let's do a few more (if we don't need the value popped, we don't need to assign it to a variable) ...

# In[ ]:


# pop two items
my_dq_stack.pop()
my_dq_stack.pop()

# push (append) a new item
my_dq_stack.append("New second item")

# check the stack
print(f"Now the stack is: {my_dq_stack}")


# ### Error handling
# Just like the List example, **if** we **try** to **pop more items than we have**, we get an **exception**.

# In[ ]:


# pop three items, but I only have two
print(my_dq_stack.pop())
print(my_dq_stack.pop())

# this one will ... BOOM!
print(my_dq_stack.pop())


# # Queues in Python

# There are **multiple ways** that you can **implement queues in Python**. In fact, it's not surprising that we can use the **same** types of **approaches** that we **used for stacks**. We are just changing which way we are inserting and retrieving from. For stacks, we inserted and removed from the same end (LIFO approach), for **queues** we we'll **insert in one end and remove from the other** (**FIFO** approach)

# ## Implementation #1: Using the built-in Python List as is
# The **standard Python List** class has all the methods you need to implement a queue. The ***append()* method** will be **equivalent to an "enqueue"**. *append()* will **keep appending to** the **end of the list**, **so** we can **envision** the **end of the list** as the **back of the queueu**. The **first element of the list** is the **front of the queue**, so **to dequeue an item**, we need to **retrieve and remove the first element**. The ***pop()*** method in List **can do that**, if we **pass "0" as an argument**. As we saw earlier, *pop()* by default removes and returns the last element in the list, but you pass an argument specifying a specific index for an item to remove.

# #### Creating my queue list 

# In[ ]:


# Create a list to implement a queue. Having "queue" somewhere in the variable will remind me I want to use it as a queue
my_plain_queue = []


# #### Enqueue elements to the queue using append()

# In[ ]:


# push a few items with append
my_plain_queue.append("First Item")
my_plain_queue.append("Second Item")
my_plain_queue.append("Third Item")
my_plain_queue.append("Fourth Item")


# #### Check my queue
# We can print the list to view the queue. Again, we have to **visualize** the **beginning as the front of the queue**, and the **end as the back**.

# In[ ]:


print(my_plain_queue)


# #### Dequeue element from the queue
# We pop using the **standard *pop()* method** in List, **passing "0" as an argument**, which pops the first element from the list.

# In[ ]:


# pop the top element from the stack
first_element = my_plain_queue.pop(0)
print(f'I just dequed "{first_element}" from the queue')

# print the queue to confirm element is gone
print(f"Now the queue is: {my_plain_queue}")


# Let's do a few more ...

# In[ ]:


# dequeue two items
my_plain_queue.pop(0)
my_plain_queue.pop(0)

# enqueue a new item
my_plain_queue.append("New second item")

# check the stack
print(f"Now the queue is: {my_plain_queue}")


# ### Error handling, or lack thereoff
# Just like with the stack implementation, we can't dequeue more than we have in the list ...

# In[ ]:


# dequque/pop three items, but I only have two
print(my_plain_queue.pop(0))
print(my_plain_queue.pop(0))

# this one will ... BOOM!
print(my_plain_queue.pop(0))


# ## Implementation #2: Custom queue class based on built-in List
# Justy like we did with stacks, we can **create** a **fancier queue class** **wrapping it around a class**. The MyQueue below adds the following "enhancements":
# - **"Legit" *enqueue()* and *dequeue()*** methods
# - ***dequeue()*** method **preventing exception**
# - Added **friendly methods** like *peek()*, *length()*, and *is_empty()*
# - Added a ***print_queue()*** method that **prints the queue with clear indicators**

# In[ ]:


class MyQueue:
    '''
    This class implements a standard Queue data structure using a Python built-in list class
    '''
    
    def __init__(self):
        '''
        Initialize the queue as an empty list
        '''
        self.list = []

    def enqueue(self, item):
        '''
        Append an item to the end of the queue using the standard append method
        '''
        self.list.append(item)


    def dequeue(self):
        '''
        Pop the first item from the queue, or None if the stack is empty
        '''
        if self.is_empty():
            return None
        else:
            return self.list.pop(0)

    def peek(self):
        '''
        Return the first item from the queue without dequeing it, or None if the queue is empty
        '''
        if self.is_empty():
            return None
        else:
            return self.list[0]

    def is_empty(self):
        '''
        Return True if queue is empty, or False if note
        '''
        return (len(self.list) == 0)
        
    def length(self):  
        '''
        Return the number of items in the queue
        '''
        return len(self.list)

    def print_queue(self):
        '''
        Print the queue with clear indicators of front and back
        '''
        # check for empty stack
        if (self.is_empty()):
            print("Queue is empty")
            return
        
        # iterate through list items
        for n in range(len(self.list)):
            # if this is the front of the queue, print an indicator
            if (n == 0):
                print("[FRONT] ", end="")
                
            # print the item
            print(self.list[n], end="")

            # if this is not the last item, print an indicator of a queue order
            if (n < len(self.list) - 1):
                print(" <-- ", end="")
            # else, just print an indicator line break
            else:
                print(" [BACK]")


# #### Creating my fancy queue object 

# In[ ]:


my_fancy_queue = MyQueue()


# #### Enqueue items into the queue, using our "legit" *queue* method

# In[ ]:


# enqueue a few items
my_fancy_queue.enqueue("First Item")
my_fancy_queue.enqueue("Second Item")
my_fancy_queue.enqueue("Third Item")
my_fancy_queue.enqueue("Fourth Item")


# #### Check my queue using my fancy *print_queue()*

# In[ ]:


my_fancy_queue.print_queue()


# Ahhhh ... so pretty ...

# #### Dequeue the front item, and check again

# In[ ]:


# pop the top element from the stack
first_element = my_fancy_queue.dequeue()
print(f'I just dequed "{first_element}" from the queue')

# print the queue to confirm element is gone
print("\nQueue now is:")
my_fancy_queue.print_queue()


# #### Try to break this one by dequeing more items than the queue has

# In[ ]:


print(my_fancy_queue.dequeue())
print(my_fancy_queue.dequeue())
print(my_fancy_queue.dequeue())
print(my_fancy_queue.dequeue())
print(my_fancy_queue.dequeue())
print(my_fancy_queue.dequeue())


# ## Implementation #3: Using the Collections module
# This will be nearly a repeat of what we did with stacks, using the **Deque** class. Recall that deque can insert and retrieve from either end, so we'll use ***append()*** to enqueue, and ***popleft()*** to dequeue.

# #### Import collections.deque
# As usual, we need to import the module to use it.

# In[ ]:


from collections import deque


# #### Creating my queue deque 

# In[ ]:


# Create a new stack using deque   
my_dq_queue = deque()


# #### Enqueue elements to the queue using append()

# In[ ]:


# enqueue a few items with append
my_dq_queue.append("First Item")
my_dq_queue.append("Second Item")
my_dq_queue.append("Third Item")
my_dq_queue.append("Fourth Item")


# #### Check my queue
# We can print the deque to view the queue. Just like with the list, we have to visualize the beginning as the front of the queue, and the end as the back.

# In[ ]:


print(my_dq_queue)


# #### Dequeue first element from the queue
# We dequeue using the ***popleft()*** method in deque, which **also returns the element** that was popped.

# In[ ]:


# dequeue the first element from the queue
first_element = my_dq_queue.popleft()
print(f'I just dequeued "{first_element}" from the queue')

# print the queue to confirm element is gone
print(f"Now the queue is: {my_dq_queue}")


# Let's do a few more ...

# In[ ]:


# dequeue/pop two items
my_dq_queue.popleft()
my_dq_queue.popleft()

# enqueue (append) a new item
my_dq_queue.append("New second item")

# check the queue
print(f"Now the queue is: {my_dq_queue}")


# ### Error handling
# Just like the List example, **if** we **try** to **dequeue more items than we have**, we get an **exception**.

# In[ ]:


# dequeue three items, but I only have two
print(my_dq_queue.popleft())
print(my_dq_queue.popleft())

# this one will ... BOOM!
print(my_dq_queue.popleft())


# In[ ]:




