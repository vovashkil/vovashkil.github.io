#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue"> Recursion Gone Wrong
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Fernando Takes down development server with bad recursion
# As it goes in movies, this is "based on a true story" when I took down my entire department development server with bad recursion. I've simplified the ticketing system a lot, but the main point is the same.

# ## Background: trouble ticketing in a real development environment
# We worked with a **typical trouble ticketing system**, where **testers** would **create trouble tickets when** they **found problems** in the software. Early in the development cycle, **developers** themselves would **create tickets during unit testing**. **Tickets** were **associated with any changes made in source control**, so you could always track what issue was associated with a change in the source code. That's a good best practice.

# ## Simple Trouble Ticket class
# This is an extreme simplification of a ticket class. A real ticket would have a vast amount of attributes, and a lot more possible states as it progresses through testing phases. But for the purpose of the recursion story, it serves the purpose.

# In[ ]:


class Ticket:
    '''
    Record a trouble ticket, with Id, description, status, and depent tickets
    '''
    def __init__(self, ticket_id, description, status = "Open"):
        self.ticket_id = ticket_id
        self.description = description
        self.status = status
        self.dependent_tickets = []

    def close(self):
        '''
        Close the ticket, but only if all of the dependent tickets are closed
        '''
        if all(ticket.status == "Closed" for ticket in self.dependent_tickets):
            self.status = "Closed"
        else:
            raise ValueError("Cannot close ticket until all dependent tickets are closed")


    def __str__(self):
        # create list of dependent ticket ids
        dep_ids = [ticket.ticket_id for ticket in self.dependent_tickets]
        
        return f"Ticket {self.ticket_id}: {self.description} ({self.status}) - Dependent tickets: {str(dep_ids)}"


# ### Create some tickets
# Let's create some sample tickets. In my story, these were software issues on a large application, but for an example, it's easier to use hardware issues anyone can relate to.

# In[ ]:


# create tickets
ticket1 = Ticket(1, "My computer displays error when booting up")
ticket2 = Ticket(2, "I can't upload files")
ticket3 = Ticket(3, "I can't download files")
ticket4 = Ticket(4, "My printer is jammed")
ticket5 = Ticket(5, "I hard drive is making strange noises")
ticket6 = Ticket(6, "I can't scan")
ticket7 = Ticket(7, "I can't email")
ticket8 = Ticket(8, "I can't log in")
ticket9 = Ticket(9, "I can't print")
ticket10 = Ticket(10, "Cannot print printer diagnostic page")

# print current tickets
print(ticket1)
print(ticket2)
print(ticket3)
print(ticket4)
print(ticket5)
print(ticket6)
print(ticket7)
print(ticket8)
print(ticket9)
print(ticket10)


# ### Close a ticket
# In a normal software development cycle, closing a ticket is not a simple one step. It will go through various states of testing, until a tester agrees the problem was resolved. But yes, ultimately it will get resolved/closed, so the simplified example is going straight there.

# In[ ]:


ticket8.close()
print(ticket8)


# Everything looks great. But **what if my ticket has a dependency**?

# #### Add a dependency to from ticket 2 to ticket 5 
# Let's say the **problem uploading** is **related to** the **hard drive issue**

# In[ ]:


# add a dependency to from ticket 2 to ticket 5
ticket2.dependent_tickets.append(ticket5)
print(ticket2)
print(ticket5)


# #### Now try to close the ticket with the dependency
# We will get an **error**, **because** we **can't close a ticket if there is a dependent one open.**. That's a actually a common good practice.

# In[ ]:


ticket2.close()


# ## Issue for developers early in the development cycle
# The dependency check above was a good practice. Testers need to make sure they closed tickets in sync. However, **early in the development cycle**, **developers** themselves **created tickets anytime** they had to **push code to source control**. That was a mandatory practice (and a good one). **These weren't bugs really**, but part of the process of creating initial versions of application code.
# 
# The **problem** was, **when** it came time to **deliver** the **code to** the official **system test team**, **developers had to move all** of those **tickets, one by one**, through various states. In the **real world** there are a **lot more intermediate states between open and close**. It was a **tedious time-consuming process**, often times made **harder**, **when** we hit one of those **ticket dependencies**.

# ## Fernando's brilliant idea: fasttrack
# I had the **brillian idea** that when it was time to deliver new software (not bug fixes), I could **close all related tickets in one shot**. I even gave it a fancy name: **fasttrack**.

# ### Fasttrack
# The **actual *fasttrack**** was written using **UNIX shell script**, and it **sequentially moved** the trouble **tickets through various states** **until** the final **"closed"** state.
# 
# This is a simplified "re-enacment" of the algorithm using Python. Note the **key recursive part**. **If** a **ticket has dependent children**, the **script would recursively call** a **new version of itself** to close that ticket first, thus avoiding that dependency error.

# In[ ]:


def fasttrack(ticket):
    '''
    Close a ticket, by recursevely closing any of its children first
    '''

    print(f"Closing ticket {ticket.ticket_id}", flush=True)
    
    # first recursively close all the children. If there are no children, we will skip to the next line, and end teh recursion
    for child_ticket in ticket.dependent_tickets:
        fasttrack(child_ticket)

    # now close the current ticket
    ticket.close()


# ### And it would have worked really well if not for ...
# This was a **solid plan**, and you can see it **works for** our **simple case earlier**.

# #### "Fasttrack" the same ticket that failed above

# In[ ]:


# try to close ticket2
fasttrack(ticket2)

# Show ticket2 is closed, as well as all its children
print(ticket2)
for ticket in ticket2.dependent_tickets:
    print(ticket)


# ### That would have worked like a charm, but let's look a these 3 tickets, and see how disaster can happen ...

# In[ ]:


# print these three tickets to setup the story below
print(ticket9)
print(ticket4)
print(ticket10)


# ### Circular dependency
# This wasn't really supposed to happen, but it **turns out in many cases** you **could end up with** what we call a **circular dependency**. In my case, those were artifically added by the ticketing system for some odd reason I can't recall. But in real cases that can happen. For instance:
# -  Print problems (**ticket9**) , **dependent on** printer jam (**ticket4**)
# -  Toubleshooting printer jam (**ticket4**), **depends** on being able to print a diagnistic page (**ticket10**)
# -  But printing a diagnostic page (**ticket10**), requires the ability to print, so it **depends back** on **ticket9**
# 
# So **ticket9 depends on ticket4, which depends on ticket 10, which depends back on ticket9**, which puts us in an **infinite loop.**

# #### Add the circular dependency example

# In[ ]:


# print and scan problems, dependent on printer jam
ticket6.dependent_tickets.append(ticket4)
ticket9.dependent_tickets.append(ticket4)

# printer jam depends on ability to print a diagnostic page
ticket4.dependent_tickets.append(ticket10)

# but printing a dignostic page depends on not being able to print
ticket10.dependent_tickets.append(ticket9)

# print these three tickets to confirm the dependencies added
print(ticket9)
print(ticket4)
print(ticket10)


# # <span style="color:red"> WARNING: EXECUTING THE NEXT CELL WILL GO ON AN INFINITE LOOP</span>
# <span style="color:red">**You will need to stop the cell or, restart the kernel, or if all fails, stop your jupyter notebook process**. In fact, you're better off not running, and just watching the video of my demo.</span>

# ### Try "fastracking" ticket9, and experience the horror Fernando felt
# I triumphally **tried my script for just one ticket** first, but as it approached that final state, it **hit a circular dependency** with other tickets. I had some simple print statements as in my demo, announcing each key step. So I **watched in horror as the print messages started filling up my screen**. Worse yet, because **these were executable scripts**, each one was a **separate UNIX process**.
# 
# **Within 30 seconds**, I could hear my officemate saying, ***"Hey, are you having a problem with the server?"***

# In[ ]:


# fasttrack ticket9, which is at the top of the circular dependency
fasttrack(ticket9)


# ## Epilogue

# I had to do a **"walk of shame" towards my system administrator's** office. As I walked in, I could hear him yelling, ***"What the hell is fasttrack?"***
# 
# Given the fact that my **fasttrack script multiplied like the mythical hydra creature**, there was no way to stop the individual processes. And the consoles were hum anyway, with all the CPUs taken by the "fasttrack virus". My **SA had to reboot the whole development server**, support multiple application teams.  

# ## Moral of the story
# In fairness to me, the fact that the ticketing system injected artificial dependencies was not something I would know. I later came to learn that the only way to move tickets forward on the very last step, was using a special tool. However, **when using recursion**, you **need to be 100% percent sure that you will hit your base case**, **or** you **can do some real damage**.  In my case, perhaps I should have had a "safety check" that counts the length of the recursion thread, and stops it past a certain point.
