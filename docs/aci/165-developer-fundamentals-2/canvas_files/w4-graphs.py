#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Graphs
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Overview

# Graphs **represent relationships between items**. They are represented by **two main elements**: 
# - **Nodes or vertices**: Represent individual objects or entities
# - **Edges**: Illustrate connections or relationships between nodes
#     - Edges can optionally have directions and weights
# 
# There are **countless real-world relationships** between entities that **can be represented by graphs**: computer networks, traffic routing, social networks, etc. 
# 
# **Once** a **graph is defined**, we **can apply algorithms** to **derive meaningful information** about it. **For instance**, on a graph that maintains the distance between cities, a **graph algorithm** can **identify** the **shortest path between two points**. That's the basis of most driving direction Maps we routinely use.

# ## Types of graphs
# There are a **multitude of different variations of graph**s. Some of the common ones include:
# - **Undirected graph** - **edges** can be **traversed in either direction**. Its edges do not have arrows on them. 
# - **Directed graph** - **edges have** a **defined direction**, denoted by arrows.
# - **Weighted graph** – a graphic with values, or **weights, on each edge**. 
# - **Cyclic graph** - a graph that **contains** at least one **cycle** (a **path that starts and ends at the same vertex**).
# - **Acyclic graph** - a graph that **contains no cycles** at all.
# - **Connected graph** - a graph where **any two nodes are connected by a path** (every example earlier was connected)
# - **Disconnected graph** - a graph where **at least two nodes are not connected** by a path.
# 
# All of the above are best visualized with a graph diagram or an example, but we'll do that as we go along in the notebook.

# # Graph representation
# **Because** there are **so many different variations** in graph, **there is no universally accepted way to represent Graphs**. I'll just show a couple of examples.

# ## Dictionary representation
# **In Python**, a **Dictionary is a popular choice**, because you can set a **node/vertex as the key**, and have the **edges to connected nodes** represented as a **list of values**.
# 
# For **example**, the undirected graph below could be represented with the following Python dictionary:
# ```
# graph["A"] = ["C"]
# graph["C"] = ["A", "G", "E"]
# graph["E"] = ["C", "G"]
# graph["G"] = ["C", "E"]
# ```

# ![graph1.png](attachment:e956fffd-12bf-4216-beaa-b76b8c5eacf6.png)

# What about **directed graphs**? And **graphs with weights**? \
# **Dictionaries will work for them as well**, with just some small variations. We'll **use this representation for all the examples** below, and see them in context.

# ## Other representations
# Again, there is no hard set rule for how to repreent a graph. The **main thing** is to have a **way to maintain both nodes and edges**. I'll provide a couple examples below, but there could be others.
# 
# **You cannot predict** which **format** an **algorithm or graphing library** you need **is expecting**. What you can do (and is what you'll see in my implementation), is **choose one way to represent the graph**, and **offer** various **methods** that **return the data in different ways**, which other libraries may need.

# ### Separate lists of nodes and edges
# An alternative way would be to **keep** a separate **list of all the nodes**, and **all the edges**. The edges can be represented as a list of tuples.
# 
# For example, for the diagram above we could represent it as:
# ```
# graph.nodes = ["A", "C", "E", "G"]
# graph.edges = [("A", "C"), ("C", G"), ("C", "E"), ("E", "G")]
# ```

# ### Adjacency Matrices
# A **quick way represent edges**, particularly **weighted edges**, is with  something called an **"adjacency matrix"**. This is **something you see used in** a number of **algorithms**. An **adjacency matric** assumes that **all nodes** are **represented by integers from 0 to *n-1***, where *n* is the **number of nodes**. In that way, you can **create an *n* by *n* two-dimensional array** (the adjacency matrix), and **each [row][col] combination** represents the **weight of an edge** between two nodes.
# 
# For example, assume we have 5 nodes. The adjacency matrix would by a 5 x 5 array looking something like this: 
# ```
# adjacency_matrix = [
#     [0, 0, 1, 2, 0],
#     [0, 2, 1, 0, 3],
#     [0, 0, 1, 7, 0],
#     [4, 5, 0, 2, 0],
#     [0, 3, 1, 2, 5],
# ]
# ```
# For this array, the weight node 2 and 3 (remembering the node numbers start at 0) would be 7. Just look at the 3rd row (index 2) and 4th column (index 3) above.
# 
# Although **my graph classes** will not be based on an adjacency matrix, they will **provide** a **get_adjacency_matrix() method** to build one as needed for algorithms.

# # Undirected Graph
# Let's start with a simple **plain undirected graph, with no weights** as we just saw above. Remember, undirected graphs are ones where edges can be traversed in either direction. 

# ## The MyGraph class
# We will **use the Dictionary format** we just saw. **Since** an **edge in** an **undirected graph has no explicit direction**, **when** we **add an edge** between two nodes, we will **add the edge to both sides**. In other other words, if we add an edge between "A" and "C", we will add "C" to the list of "A" edges, and we will add "A" to the list of "C" edges.

# In[ ]:


class MyGraph:
    '''
    Simple graph class storing a dictionary representation of a graph, and supporting 
    methods to add nodes and print
    '''
    def __init__(self):
        '''
        Initialize an empty dictionary to store the graph.
        The graph is a dictionary where the keys are nodes, and the values are lists of adjacent nodes.

        Example:
            graph["A"] = ["B", "C"]
            means there is an edge from "A" to "B" and "C"
        '''
        
        self.graph = {}

    def add_edge(self, from_node, to_node):
        '''
        This method adds an edge between two nodes in the graph.

        '''

        # if the "from_node" or "to_node" are not in the dictionary yet, add an entry
        if from_node not in self.graph:
            self.graph[from_node] = []
        if to_node not in self.graph:
            self.graph[to_node] = []
            
        # appends 'to_node' to the list of neighbors for the 'from_node', unless it's already there
        if (to_node not in self.graph[from_node]):
            self.graph[from_node].append(to_node)

        # since this is an undirected graph, we add the reverse edge as well.
        if (from_node not in self.graph[to_node]):
            self.graph[to_node].append(from_node)
    
    def set_graph(self, graph):
        '''
        Set the graph with a complete graph representation
        '''
        self.graph = graph
    
    def get_graph(self):
        '''
        Returns the complete graph representation as a Dictionary
        '''
        return self.graph

    def get_nodes(self):
        '''
        This method returns a list of all the nodes in the graph.
        '''
        return list(self.graph.keys())

    def get_edges(self):
        '''
        This method returns a list of all the edges in the graph.
        Each edge is represented as a tuple with the two nodes.
        '''
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((node, neighbor))
        return edges

    def get_node_edges(self, node):
        '''
        This method returns a list of all the edges from this node.
        Each edge is represented as a tuple with the two nodes.
        '''
        if node in self.graph:
            return self.graph[node]
        else:
            return []

    def is_directed(self):
        '''
        This method returns True if the graph is directed, False otherwise.
        '''
        return False
        
    def print_graph(self):
        '''
        Print the vertices and edges of the graph
        '''
 
        for node in self.graph:
            print(f'{node} <--> {self.graph[node]}')
            
    def print_edges(self):
        '''
        Print the edges of the graph
        '''
        for edge in self.get_edges():
            print(f'{edge[0]} <--> {edge[1]}')


# ## Example - friends on social media network
# Let's **use** our **MyGraph** class **to represent** a **social media network**. First we will **look at the type of social media** where diferent **users** can connect and become **"friends" of each other**. This is generally an **undirected relationship**, because if someone is your friend, you are also their friend. 
# 
# **Later** we **will look at** the example of **"following" someone**", which is a one sided relationship (we'll see that later).

# ### SocialUser Class
# I'll create a simple class to store users of my social media application.

# In[ ]:


class SocialUser:
    '''
    Simple class to store the information about a social media user.
    '''
    
    def __init__(self, user_id, name, email, friends = []):
        '''
        Initialize the user with an id, name, and a list of friends.
        
        Parameters:
            user_id (str): Unique identifier for the user
            name (str): Name of the user
            email (str): Email address of the user
            friends (list): List of user IDs representing the user's friends
        '''
        
        self.user_id = user_id
        self.name = name
        self.email = email
        self.friends = friends

    def add_friend(self, friend):
        '''
        Add a friend to the user's list of friends.
        '''
        self.friends.append(friend)

    def __str__(self):
        '''
        String representation of the user.
        '''
        return f'{self.name} -> {self.friends}'


# ### Create some users
# Let's create 10 users with somewhat random data, and add them to a list of users.

# In[ ]:


user1 = SocialUser("alejandro_rosalez", "Alejandro Rosalez", "alejandro_rosalez@example.com", 
                   ["jane_doe", "carlos_salazar"])
user2 = SocialUser("akua_mansa", "Akua Mansa", "akua_mansa@example.com", 
                   ["martha_rivera","efua_owusu","arnav_desai","diego_ramirez"])
user2 = SocialUser("martha_rivera", "Martha Rivera", "martha_rivera@example.com", 
                   ["akua_mansa","arnav_desai","efua_owusu"])
user3 = SocialUser("mary_major", "Mary Major", "mary_major@example.com", 
                   ["gil_dong_hong","terry_whitlock"])
user4 = SocialUser("arnav_desai", "Arnav Desai", "arnav_desai@example.com", 
                   ["martha_rivera","diego_ramirez","akua_mansa","jane_doe"])
user5 = SocialUser("carlos_salazar", "Carlos Salazar", "carlos_salazar@example.com", 
                   ["alejandro_rosalez","terry_whitlock","gil_dong_hong"])
user6 = SocialUser("diego_ramirez", "Diego Ramirez", "diego_ramirez@example.com", 
                   ["arnav_desai","akua_mansa"])
user7 = SocialUser("efua_owusu", "Efua Owusu", "efua_owusu@example.com", 
                   ["akua_mansa","martha_rivera"])
user8 = SocialUser("gil_dong_hong", "Gil-dong Hong", "gil-dong_hong@example.com", 
                   ["mary_major","carlos_salazar"])
user9 = SocialUser("jane_doe", "Jane Doe", "jane_doe@example.com", 
                   ["alejandro_rosalez","arnav_desai"])
user10 = SocialUser("terry_whitlock", "Terry Whitlock", "terry_whitlock@example.com", 
                    ["mary_major","carlos_salazar"])


# In[ ]:


# add all my users to a list
users_list = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]


# ### Create graph to represent relationships
# Let's **use** our **MyGraph** class to **represent** all my **users'relationships**. Each user will become a node, and each friend relationship becomes an edge.

# In[ ]:


# create graph to represent relationships
social_graph = MyGraph()

# iterate through each user
for user in users_list:
    # iterate through each friend of the user
    for friend in user.friends:
        # add an edge between the user and their friend
        social_graph.add_edge(user.user_id, friend)


# Ok, so **now I have a graph**. Or do I? How do I even see what I have?
# 
# **Next**, we'll look at  **how to visualize** the graph.
# 
# But, **more importantly**, now that we **have the information properly represented as a graph**, we will be **able to derive conclusions** from it, **using** different **algorithms**. We'll **come back to those later**.

# ### Visualize the graph
# **Much of of what will do with a graph revolves around obtaining information from it**, rather than visualizing it. But sometimes a **visualization helps for debugging**, or **making** some **basic observations**. **Python does not have a built-in graphing library**. So we have **two options**:
# - Provide a **simple text based representation** of the graph
# - **Use** one of many **external** Python **libraries** to draw a graph

# #### Basic text output
# A basic text output will just need to **show each node, and** the **neighbors they have an edge to**. Our graph class has a method for that.

# In[ ]:


# print text representation of the final graph
social_graph.print_graph()


# We **can also print** all the **individual edges**. In some cases that's beneficial.

# In[ ]:


# print text representation of the final graph
social_graph.print_edges()


# #### Graphic representation with external library
# **There are a number of external Python libraries** to **represent and display graphs**. A basic **internet search** such for something like ***"visualize network graphs in python"*** will provide **many options** you can choose from.
# 
# **I've used** one such **library**, and **implemented** a simple **function to display my graphs**. The main thing the **library needs** is a **list of the nodes and edges**. The rest is just a bit of tweaking of appearance, and a **visual represenation will be printed**. However, being that **this is an external library**, and **NOT a built-in part of Python**, I **will not include** that **implementation in the notebook**. I'll leave this block of code commented out, and use it only in live demos. If by any chance I forget to comment out, just ignore the exception you'll get in the next cell, since you won't have my function.
# 
# Although **what you install in your environment is entirely up to you**, I will say that the **installation and use** of the libary I selected (the most common way mentioned in the internet searches) was **not very hard**:
# - A simple pip install to install the library
# - A few lines of code copied from examples
# - A little bit of time tweaking the output to what I wanted

# In[ ]:


# Import module with functions to display visual representation of my graph
# The module is my own, but the functions use a popular network graph utility 
#import graph_printer as gp

# display graph with nodes and edges from my SimpleGraph object
#gp.draw_graph(social_graph.get_nodes(), social_graph.get_edges())


# I've **included** a **screenshot** of the **graph I got when running in my environment** (the node position can change on each run). If we **look at the picture**, and **compare to our text print out**, we see **they match**. For **example**, if I look at **"mary_major"** on the graph, I see **connections to "gil_dong_hong" and "terry_whitlock"**. If I look at the my previous **text output**, I'll see the **same thing**.

# ![networkx1.png](attachment:e2b239c4-e49d-4b7f-8fcf-42fd57dc68ef.png)

# I may not bother printing all the subsequent graphs in the notebook. Remember, the **graphs** are **nice to look at**, **but** the **information** we'll get **from** the upcoming **algorithms** is **where** the **real value is**.

# # Directed Graph
# No let's represent a directed graph. **Directed graphs** are ones where **edges have a specific direction**, as seen in the example below.

# ![graph2.png](attachment:d863ae26-098b-479c-a034-644eb48c1904.png)

# ## Updated MyGraph class
# As it turns out, we **can use** pretty much the **same Dictionary format** for directed graphs. The **only difference** is that now if we add an adge from "A" to "C", we **won't automatically add** the **reverse** "C" to "A" **edge** as we did in the previous example.
# 
# For **example**, the directed graph above will be represented with the following Python dictionary:
# ```
# graph["A"] = ["B", "C"]
# graph["B"] = ["A", "C"]
# graph["C"] = ["D"]
# graph["D"] = ["B", "C"]
# ```
# Note that "C" is in the list of "A" edges, because there is an edge from "A" to "C", but "A" does not appear in "C"s list.
# 
# We could create a new class, but instead we'll just **enhance** the **existing MyGraph** by **adding** an **attribute** at construction time, **to indicate whether it is directed**.

# In[ ]:


class MyGraph:
    '''
    Simple graph class storing a dictionary representation of a graph, and supporting 
    methods to add nodes and print
    '''
    def __init__(self, directed = False):
        '''
        Initialize an empty dictionary to store the graph.
        The graph is a dictionary where the keys are nodes, and the values are lists of adjacent nodes.

        Example:
            graph["A"] = ["B", "C"]
            means there is an edge from "A" to "B" and "C"

        Parameters:
            directed (bool): If True, the graph is directed. Default is False.
        '''
        self.directed = directed
        self.graph = {}

    def add_edge(self, from_node, to_node):
        '''
        This method adds an edge between two nodes in the graph.

        '''
        
        # if the "from_node" or "to_node" are not in the dictionary yet, add an entry
        if from_node not in self.graph:
            self.graph[from_node] = []
        if to_node not in self.graph:
            self.graph[to_node] = []
  
        # appends 'to_node' to the list of neighbors for the 'from_node', unless it's already there
        if (to_node not in self.graph[from_node]):
            self.graph[from_node].append(to_node)

        # if the graph is undirected, repeat the code to add the reverse edge as well
        if not self.directed:
            if (from_node not in self.graph[to_node]):
                self.graph[to_node].append(from_node)

    def set_graph(self, graph):
        '''
        Set the graph with a complete graph representation
        '''
        self.graph = graph

    def get_graph(self):
        '''
        Returns the complete graph representation as a Dictionary
        '''
        return self.graph
        

    def get_nodes(self):
        '''
        This method returns a list of all the nodes in the graph.
        '''
        return list(self.graph.keys())

    def get_edges(self):
        '''
        This method returns a list of all the edges in the graph.
        Each edge is represented as a tuple with the two nodes.
        '''
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((node, neighbor))
        return edges
        

    def get_node_edges(self, node):
        '''
        This method returns a list of all the edges from this node.
        Each edge is represented as a tuple with the two nodes.
        '''
        if node in self.graph:
            return self.graph[node]
        else:
            return []

    def is_directed(self):
        '''
        This method returns True if the graph is directed, False otherwise.
        '''
        return self.directed
        
    def print_graph(self):
        '''
        Print the vertices and edges of the graph
        '''

        # use a different arrow to indicate directed and undirected
        if (self.directed):
            arrow_str = "-->"
        else:
            arrow_str = "<-->"
 
        for node in self.graph:
            print(f'{node} {arrow_str} {self.graph[node]}')


    def print_edges(self):
        '''
        Print the edges of the graph
        '''
        # use a different arrow to indicate directed and undirected
        if (self.directed):
            arrow_str = "-->"
        else:
            arrow_str = "<-->"
            
        for edge in self.get_edges():
            print(f'{edge[0]} {arrow_str} {edge[1]}')


# ## Example - social media followers
# We will use our updated our updated **MyGraph** class **to represent** the type of **social media were users post updates**, and other **users can follow them**. That **"following" relationship is directed**, because a user can follow another, and not be followed back.

# ### SocialPoster Class
# I'll make a small change to my user class, to supporting following, instead of friends.

# In[ ]:


class SocialPoster:
    '''
    Simple class to store the information about a social media user.
    '''
    
    def __init__(self, user_id, name, email, following = []):
        '''
        Initialize the user with an id, name, and a list of users being followed by this user.
        
        Parameters:
            user_id (str): Unique identifier for the user
            name (str): Name of the user
            email (str): Email address of the user
            following (list): List of user IDs this use is following
        '''
        
        self.user_id = user_id
        self.name = name
        self.email = email
        self.following = following

    def follow(self, user_id):
        '''
        Add a user ID to the list of users being followed by this user.
        '''
        self.following.append(user_id)

    def __str__(self):
        '''
        String representation of the user.
        '''
        return f'{self.name} -> {self.following}'


# ### Create some posters
# Let's create 10 posters with somewhat random data, and add them to a list of posters.

# In[ ]:


poster1 = SocialPoster("john_stiles", "John Stiles", "john_stiles@example.com",
                       ["jorge_souza", "pat_candella", "sofia_martinez", "wei_zhang"])
poster2 = SocialPoster("jorge_souza", "Jorge Souza", "jorge_souza@example.com",
                       ["john_stiles"])
poster3 = SocialPoster("kwaku_mensah", "Kwaku Mensah", "kwaku_mensah@example.com",
                       ["pat_candella", "sofia_martinez", "wei_zhang", "marcia_oliveria"])
poster4 = SocialPoster("mateo_jackson", "Mateo Jackson", "mateo_jackson@example.com",
                       ["richard_roe", "jorge_souza"])
poster5 = SocialPoster("pat_candella", "Pat Candella", "pat_candella@example.com", 
                       ["john_stiles", "jorge_souza", "marcia_oliveria"])
poster6 = SocialPoster("paulo_santos", "Paulo Santos", "paulo_santos@example.com", 
                       ["kwaku_mensah", "wei_zhang"])
poster7 = SocialPoster("richard_roe", "Richard Roe", "richard_roe@example.com", [])
poster8 = SocialPoster("sofia_martinez", "Sofía Martínez", "sofia_martinez@example.com", 
                       ["pat_candella", "wei_zhang"])
poster9 = SocialPoster("wei_zhang", "Wei Zhang", "wei_zhang@example.com", 
                       ["paulo_santos"])
poster10 = SocialPoster("marcia_oliveria", "Marcia Oliveria", "marcia_oliveria@example.com", 
                        ["paulo_santos", "richard_roe"])


# In[ ]:


# add all my users to a list
users_list = [poster1, poster2, poster3, poster4, poster5, poster6, poster7, poster8, poster9, poster10]


# ### Create graph to represent relationships
# Once again, we'll **use** our **MyGraph** class to **represent** all my **users'relationships**. This time we **construct** our **object** as a **directed graph**.

# In[ ]:


# create graph to represent relationships
poster_graph = MyGraph(directed = True)

# iterate through each poster user
for user in users_list:
    # iterate user being followed by this user
    for followed in user.following:
        # add an directed edge fron this user to the poster user being followed
        poster_graph.add_edge(user.user_id, followed)


# ### Visualize the graph
# Once again, we'll quickly visualize the graph as we did earlier.

# #### Basic text output
# A basic text output will just need to **show each node, and** the **neighbors they have an edge to**. Our graph class has a method for that.

# In[ ]:


# print text representation of the final graph
poster_graph.print_graph()


# We can quickly **observe** that **since** this is an **directed graph**, we **won't automatically see** the **reverse edge for each connected node**. For instance, "marcia_oliveira" follows ""paulo_santos", but "paulo_santos does not follow "marcia_oliveira".

# #### Graphic representation with external library
# Once again, I'm **using my library** to print the graph, **which uses** a **popular Python graphing library**. Note that I have an extra attribute now that specifies that the graph is directed. This is something that the external library I'm using supports.
# 
# And again ... **I'll have this line commented out** when I'm not demoing.

# In[ ]:


# display graph with nodes and edges from my SimpleGraph object
#gp.draw_graph(poster_graph.get_nodes(), poster_graph.get_edges(), directed = True)


# I've **included** a **screenshot** of the **graph I got when running in my environment**. If we **look at the picture**, **now** we **see arrows with specific directions**, that match what we see in our text output. If we look at **"paulo_santos"**, we see a **bi-directional arrow with "wei_zhang"**, because they **both follow each other**. **But** you **only** see an **incoming arrow from "marcia_oliveira"**, because **"paulo_santos"** **does not follow "marcia_oliveria"**.

# ![networkx2.png](attachment:c20f1be3-bdb4-4b2c-b976-b093eebb1a6e.png)

# Once again, this is only part of the story. What we do with the graphs later is the rest.

# # Weighted Directed Graph
# A **weighted graph** is one where the **edges have associated weights**, or values. This can **apply to both directed or undirected** graphs. We will look at a weighted directed graph first. Below is an example for our previous directed graph example. Now each edge has a weight.

# ![networkx3.png](attachment:4961ea07-7e2b-4a2d-90cc-b42051ef7d01.png)

# ## MyWeightedGraph class
# We **could have** further **enhanced** the **original MyGraph** class to support weighted graphs. We would need a few more if statements around the code to deal with both cases. However, **to keep the code cleaner**, we'll **create** a very **similar class**, but **tweak** it **to support weights**.
# 
# We'll **still use** a **Dictionary**, largely as we did before, with **each node being** a **key**. However in this case, the **values** will be **list of tuples**, for **each connected node and the weight**. For **example**, the weighted directed graph above will be represented with the following Python dictionary:
# ```
# graph["A"] = [("B", 5), ("C", 6)]
# graph["B"] = [("A", 8), ("C", 12]
# graph["C"] = [("D", 4)]
# graph["D"] = [("B", 5), ("C", 2)]
# ```
# The **same approach would work for** a **weighted undirected graph**. In that case, the weights would just be repeated in both directions.

# In[ ]:


class MyWeightedGraph:
    '''
    Simple graph class storing a dictionary representation of a graph, and supporting 
    methods to add nodes and print
    '''
    def __init__(self, directed = False):
        '''
        Initialize an empty dictionary to store the graph.
        The graph is a dictionary where the keys are nodes, and the values are lists of adjacent nodes.

        Example:
            graph["A"] = [("B", 5), ("C", 6)]
            means there is an edge from "A" to "B" with weight 5, and "C" with weight 6 and "C"

        Parameters:
            directed (bool): If True, the graph is directed. Default is False.
        '''
        self.directed = directed
        self.graph = {}

    def add_edge(self, from_node, to_node, weight):
        '''
        This method adds an edge between two nodes in the graph.

        '''
        # if the "from_node" or "to_node" are not in the dictionary yet, add an entry
        if from_node not in self.graph:
            self.graph[from_node] = []
        if to_node not in self.graph:
            self.graph[to_node] = []
            
        # appends tuple with 'to_node' and weight to the list of neighbors for the 'from_node', unless it's already there
        if (self.get_edge_weight(from_node, to_node) is None):
            self.graph[from_node].append((to_node,weight))

        # if the graph is undirected, repeat the code to add the reverse edge as well
        if not self.directed:
            if (self.get_edge_weight(to_node, from_node) is None):
                self.graph[to_node].append((from_node,weight))
                
    def set_graph(self, graph):
        '''
        Set the graph with a complete graph representation
        '''
        self.graph = graph

    @staticmethod
    def create_from_unweighted(unweighted_graph, default_weight = 1):
        '''
        Create a weighted graph based on an uneighted graph, by assigning a default weight to all edges.
        '''

        # create a new weighted graph
        weighted_graph = MyWeightedGraph(directed = unweighted_graph.is_directed())

        # iterate through all the node and corresponding edges in the unweighted graph
        for node, edges in unweighted_graph.get_graph().items():
            # iterate through each neighbor edge, and add an edge with the default weight to this graph
            for edge in edges:
                weighted_graph.add_edge(node, edge, default_weight)

        return weighted_graph

    def get_graph(self):
        '''
        Returns the complete graph representation as a Dictionary
        '''
        return self.graph        


    def get_nodes(self):
        '''
        This method returns a list of all the nodes in the graph.
        '''
        return list(self.graph.keys())

    def size(self):
        '''
        Returns the size of the graph (number of nodes)
        '''
        return len(self.graph)

    def map_numbers_to_nodes(self):
        # return a list of numbered nodes representing the key order
        num_to_node = {}
        for index, key in enumerate(self.graph):
            num_to_node[index] = key
        
        return num_to_node
        
    def map_nodes_to_numbers(self):
        # return a list of numbered nodes representing the key order
        node_to_num = {}
        for index, key in enumerate(self.graph):
            node_to_num[key] = index
        
        return node_to_num
        
    def get_adjacency_matrix(self):
        '''
        Many algorithms expect nodes to be simple numbers, and they represent the edges of these
        nodes as a two-dimensional matrix. The value in the matrix is weight of the edge between nodes. 
        '''
        # initialize an adjacency matrix
        size = self.size()
        adj_matrix = [[0] * size for _ in range(size)]

        # get mapping of nodes values to numbered nodes
        node_map = self.map_nodes_to_numbers()

        # iterate through all the nodes and corresponding edges in the graph
        for edge in self.get_edges():
            # retrieve the nodes and weight from the edge tuple
            node1, node2, weight = edge
            # conver the nodes to onde indexes as expected for the matrix
            node1_idx = node_map[node1]
            node2_idx = node_map[node2]
            
            # add the weight to the adjacency matrix, at the 
            adj_matrix[node1_idx][node2_idx] = weight
            
        return adj_matrix

    def get_edges(self):
        '''
        This method returns a list of all the edges in the graph.
        Each edge is represented as a tuple with the two nodes and the weight.
        '''
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((node, neighbor[0], neighbor[1]))
        return edges
        
    def get_node_edges(self, node):
        '''
        This method returns a list of all the edges from this node.
        Each edge is represented as a tuple with the two nodes and the weight.
        '''
        if node in self.graph:
            return self.graph[node]
        else:
            return []
            
    def get_edge_weight(self, from_node, to_node):
        '''
        This method returns the weight of the edge between two nodes in the graph, or None
        if there is no edge between them.

        '''
        for neighbor in self.graph[from_node]:
            if neighbor[0] == to_node:
                return neighbor[1]
        return None
            
    def print_graph(self):
        '''
        Print the vertices and edges of the graph
        '''

        # use a different arrow to indicate directed and undirected
        if (self.directed):
            arrow_str = "-->"
        else:
            arrow_str = "<-->"
 
        for node in self.graph:
            print(f'{node} {arrow_str} {self.graph[node]}')

    def print_edges(self):
        '''
        Print the edges of the graph
        '''
        # use a different arrow start to indicate directed and undirected
        if (self.directed):
            arrow_str = "-->"
        else:
            arrow_str = "--"

        # build list of edges to print
        edges_to_print = []
        for edge in self.get_edges():
            # if graph is undirected, check for duplicate edges
            if (not self.directed):
                # generate reverse edge
                reverse_edge = (edge[1], edge[0], edge[2])

                # if the reverse edge is already in the list, skip
                if (reverse_edge in edges_to_print):
                    continue

            # add edge to list to print
            edges_to_print.append(edge)
            
        for edge in edges_to_print:
            # retrieve the nodes and weight from the edge tuple
            node1, node2, weight = edge
            # print the edge with the weight in between
            print(f'{node1} --({weight:3}){arrow_str} {node2}')


# ## Example - NJ driving times
# For this example, we will **create a graph** to **represent driving times between** a **few cities** around my area **in NJ**. I **created** the **map below myself**, and I **picked among cities** that have some **special meaning to me**, and also added the larger neighboring cities of Philadelphia and New York for context.

# ![nj_map.png](attachment:de8a5e12-483c-47df-b737-4cd889ea33ef.png)

# ### Record driving times
# I **collected** the **driving times between various cities** I've driven around, based on checks around 9:00am EST. As one might expect, in many cases the **driving time changes depending on the direction** of traffic. **If** I **was creating a graph with driving distances**, it **would be** an **undirected** graph, since distances are the same. **But in this case**, it will have to be a **directed graph**, to record the acurate times in both directions.
# 
# The **following dictionary represents the driving times** between every city. It's already in the format that will work for graph class.

# In[ ]:


driving_times = {
    "Freehold": [("Matawan", 23), ("Princeton", 41), ("Trenton", 40), ("Newark", 59), ("Red Bank", 29), ("New Brunswick", 41), ("Metuchen", 39)],
    "Matawan": [("Freehold", 23), ("Princeton", 56), ("Trenton", 57), ("Newark", 39), ("Red Bank", 22), ("New Brunswick", 36), ("Metuchen", 37)],
    "Princeton": [("Freehold", 37), ("Matawan", 57), ("Trenton", 18), ("Newark", 68), ("Red Bank", 70), ("New Brunswick", 19), ("Metuchen", 45)],
    "Trenton": [("Freehold", 42), ("Matawan", 56), ("Princeton", 18), ("Newark", 68), ("Red Bank", 58), ("New Brunswick", 19), ("Metuchen", 48)],
    "Newark": [("Freehold", 53), ("Matawan", 37), ("Princeton", 66), ("Trenton", 66), ("Red Bank", 51), ("New Brunswick", 42), ("Metuchen", 31)],
    "Red Bank": [("Freehold", 30), ("Matawan", 23), ("Princeton", 68), ("Trenton", 60), ("Newark", 52), ("New Brunswick", 44), ("Metuchen", 34)],
    "New Brunswick": [("Freehold", 39), ("Matawan", 32), ("Princeton", 19), ("Trenton", 19), ("Newark", 42), ("Red Bank", 46), ("Metuchen", 22)],
    "Metuchen": [("Freehold", 37), ("Matawan", 28), ("Princeton", 45), ("Trenton",49), ("Newark", 32), ("Red Bank", 36), ("New Brunswick", 22)]
}


# ### Create Graph for my NJ commute
# The driving time dictionary is already in the perfect format for me to iterate and create the graph.

# In[ ]:


# create graph to represent driving times
nj_drive_graph = MyWeightedGraph(directed = True)

# iterate through each city node in my driving_times dictionary
for city in driving_times:
    # iterate through each neighbor of the city
    for neighbor in driving_times[city]:
        # add an edge between the city and the neighbor with the driving time
        nj_drive_graph.add_edge(city, neighbor[0], neighbor[1])


# ### Visualize the graph
# Once again, we'll quickly visualize the graph as we did earlier.

# #### Basic text output
# A basic text output will just need to **show each node, and** the **neighbors they have an edge to**. Our graph class has a method for that.

# In[ ]:


# print text representation of the final graph
nj_drive_graph.print_graph()


# We can quickly **observe** that **since** this is an **directed graph**, we **won't automatically see** the **reverse edge for each connected node**. For instance, "marcia_oliveira" follows ""paulo_santos", but "paulo_santos does not follow "marcia_oliveira".

# We **can also print** all the **individual edges**. In some cases that's beneficial.

# In[ ]:


# print text representation of the final graph
nj_drive_graph.print_edges()


# #### Graphic representation with external library
# Once again, I'm **using my library** to print the graph, **which uses** a **popular Python graphing library**. Note that I have an extra attribute now that specifies that the graph is weighted. This is something that the external library I'm using supports.
# 
# And again ... **I'll have this line commented out** when I'm not demoing.

# In[ ]:


# display graph with nodes and edges from my SimpleGraph object
#gp.draw_graph(nj_drive_graph.get_nodes(), nj_drive_graph.get_edges(), directed = True, weighted = True)


# I've **included** a **screenshot** of the **graph I got when running in my environment**. This is getting very busy, but it's still cool to see. **More important than the picture** will be later on when I can **use** an **algorithm to optimize my driving times**.

# ![networkx4.png](attachment:e61608a1-65d4-468f-a752-bb211269688e.png)

# # Weighted Undirected Graph
# A **weighted undirected graph** is will work the same way as a directed one, except that the **weight applies to both directions**. So we will **use** the **same representation** mechanism, and the **same MyWeighterGraph class**.

# ## Example - wiring a local network (LAN)
# **Network design** is a very **common application of graph theory**. In this example, we will **see how we represent** a l**ocal area network using a graph**, and how we will **later** use the graph to **help in the physical wiring**.

# ### Represent possible network paths in a graph
# In the **previous examples**, I **manually added nodes and edges**. Realistically, **in most cases there are too many** nodes and edges to add. So **graphs** are generally **constructed through** some type of automated **software**. Since graphs can represent a multitude of different scenarios, there isn't an exact mechanism for that. I'll show an **example** below of how I'll **use my own program** to **create a graph to represent possible network paths** connecting workstations in building floor.
# 
# For our example, **imagine** that I have **the following layout**, where the various **3 character strings** (A01, D06, Y09, etc) **represent workstation locations** that **need to be connected** in a LAN.

# ![graph6.png](attachment:27dd0a62-dfc6-4a45-9b29-6848f825b767.png)

# Now imagine that any adjacent workstation can be connected to each other. We can also connect workstations separated by a hallway. So all of my possible network paths can be represented with this graph, where the blue lines are the edges between the workstations (which are the nodes).

# ![graph7.png](attachment:6c39a051-8765-4fe7-ab14-5e4513cdc255.png)

# Obviously there is a **very large number of nodes and edges** to created, which we do not want to do manually. So I'll **use my own way** to **encode that graph programatically**.

# #### Floor plan representation
# I defined **my own floor plan representation**. Again, this is not any kind of standard, but simply the way I'm choosing to do it. In this represention, I use a **two-dimensional array** (implemented with a Python List). In this representation:
# - **Walls** are represented with a **"WWW"** cell. In my format, I **require double walls around the plan**. This will simplify the code, and avoid out of bound indexes.
# - **Hallways** are represented with a **"   "** cell
# - **Workstartion locations** are represented with **3 character string** we see in the image.

# In[ ]:


first_floor_plan = [
    ["WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW"],
    ["WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW"],
    ["WWW","WWW","X01","X02","X03","X04","X05","X06","X07","X08","X09","X10","X11","X12","WWW","WWW"],
    ["WWW","WWW","A01","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","H01","WWW","WWW"],
    ["WWW","WWW","A02","   ","B02","C02","   ","D02","E02","   ","F02","G02","   ","H02","WWW","WWW"],
    ["WWW","WWW","A03","   ","B03","C03","   ","D03","E03","   ","F03","G03","   ","H03","WWW","WWW"],
    ["WWW","WWW","A04","   ","B04","C04","   ","D04","E04","   ","F04","G04","   ","H04","WWW","WWW"],
    ["WWW","WWW","A05","   ","   ","   ","   ","D05","E05","   ","   ","   ","   ","H05","WWW","WWW"],
    ["WWW","WWW","A06","   ","B06","C06","   ","D06","E06","   ","F06","G06","   ","H06","WWW","WWW"],
    ["WWW","WWW","A07","   ","B07","C07","   ","D07","E07","   ","F07","G07","   ","H07","WWW","WWW"],
    ["WWW","WWW","A08","   ","B08","C08","   ","D08","E08","   ","F08","G08","   ","H08","WWW","WWW"],
    ["WWW","WWW","A09","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","H09","WWW","WWW"],
    ["WWW","WWW","Y01","Y02","Y03","Y04","Y05","Y06","Y07","Y08","Y09","Y10","Y11","Y12","WWW","WWW"],
    ["WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW"],
    ["WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW","WWW"]
]


# #### Create a function to populate a Graph with possible network connections
# Now I'll **write code** to **create** a **graph from** a **representation like** the **above** one. I'll **put** that **into a function**, because I would want to do that for all the floors in my building. My **network design** will be **based on the following rules**:
# - A **workstation location** can **only** be **connected to one workstation** location **imediately around it** (excluding diagonals). In those cases, we will use a **weight of 1** to indicate the close proximity.
# - **If there is a space or wall** next to it, a wire **can go on more space over** to connect to another workstation. In those cases, we will use a **weight of 2** to indicate the extra distance.
# 
# For **example**, in the plan above, workstation ***B06*** **can connect to** ***A06***, ***B04***, ***C06***, or ***B07***.

# In[ ]:


WALL = "WWW"
HALLWAY = "   "

def is_workstation(cell):
    '''
    Check if the cell is a workstation location.
    '''
    return cell != WALL and cell != HALLWAY
    
def graph_network(graph, floor_plan):
    '''
    Create a network graph based on a floor plan.
    '''
    # iterate through each row in the floor plan (skipping walls)
    for row in range(2, len(floor_plan) - 2):
        # iterate through each column in the floor plan
        for col in range(2, len(floor_plan[row]) - 2):
            # if the current cell is a workstation location
            if is_workstation(floor_plan[row][col]):
                # if the cell above is not a wall or hallway, add edge to it
                if floor_plan[row - 1][col] != WALL and floor_plan[row - 1][col] != HALLWAY:
                    graph.add_edge(floor_plan[row][col], floor_plan[row - 1][col], 1)
                # else, try one more cell over
                elif is_workstation(floor_plan[row - 2][col]):
                    graph.add_edge(floor_plan[row][col], floor_plan[row - 2][col], 2)

                # if the cell below is not a wall or hallway, add edge to it
                if floor_plan[row + 1][col] != WALL and floor_plan[row + 1][col] != HALLWAY:
                    graph.add_edge(floor_plan[row][col], floor_plan[row + 1][col], 1)
                # else, if there is a hallway, try one more cell over
                elif is_workstation(floor_plan[row + 2][col]):
                    graph.add_edge(floor_plan[row][col], floor_plan[row + 2][col], 2)

                # if the cell to the right is not a wall or hallway, add edge to it
                if floor_plan[row][col + 1] != WALL and floor_plan[row][col + 1] != HALLWAY:
                    graph.add_edge(floor_plan[row][col], floor_plan[row][col + 1], 1)
                # else, if there is a hallway, try one more cell over
                elif is_workstation(floor_plan[row][col + 2]):
                    graph.add_edge(floor_plan[row][col], floor_plan[row][col + 2], 2)

                # if the cell to the left is not a wall or hallway, add edge to it
                if floor_plan[row][col - 1] != WALL and floor_plan[row][col - 1] != HALLWAY:
                    graph.add_edge(floor_plan[row][col], floor_plan[row][col - 1], 1)
                # else, if there is a hallway, try one more cell over
                elif is_workstation(floor_plan[row][col - 2]):
                    graph.add_edge(floor_plan[row][col], floor_plan[row][col - 2], 2)


# #### Create the graph for the floor plan
# Now we simply **create** on of our **MyWeightedGraph graphs**, and **use** the **function** above **to populate it with** our **floor plan**.

# In[ ]:


# create graph to represent floor plan
floor_plan_graph = MyWeightedGraph(directed = False)

# populate graph with floor plan
graph_network(floor_plan_graph, first_floor_plan)


# ### Visualize the graph
# Once again, we'll quickly visualize the graph as we did earlier.

# #### Basic text output

# In[ ]:


# print text representation of the final graph
floor_plan_graph.print_graph()


# If we **select a few nodes**, we can **see they represent** the **rule I described**. Look for the "B06" node for instance, and see that it will have the connections we mentioned earlier in our example.

# #### Graphic representation with external library
# Once again, I'm **using my library** to print the graph. In this case, it's a **good demonstration** of **why printing the graph** is **not always helpful**. There are **so many connections** here, the **graph adds no value**.
# 
# At the risk of sounding repetitive, the **value of representing** the possible **wirings as a graph** will be in the **algorithms we can apply** to it.

# In[ ]:


# display graph with nodes and edges from my SimpleGraph object
#gp.draw_graph(floor_plan_graph.get_nodes(), floor_plan_graph.get_edges(), weighted = True, circular = False)


# And here is the usual screen shot.

# ![networkx5.png](attachment:6748d93f-8a29-49dd-9888-f6d48eb6e667.png)

# ## Example - delivery driver routes
# In this final example, we will look at another real use case, which is **optimizing truck delivery routes**. Assume you have a **driver** that **leaves a warehouse** in the morning, and must **make deliveries to multiple locations** before returning to the warehouse. Identifying the most effective route starting at the warehouse, and returning to it, is a common problem.
# 
# We will **look at** the **algorithm to solve** that **problem soon**, but **first** we **need to represent every possible route** **using** a **graph**. Any two locations are reacheable in a map, but what will change is the distance between them. So our **graph will have every location** (plus the warehouse) **connected to each other**, but with **different weights** representing the **distance**. We could have also used driving times, but I already did that earlier.
# 
# The diagram below is an example of the graph for the warehouse and 3 delivery locations.

# ![graph4.png](attachment:0ed9acb9-d0f3-428a-804b-6ffb7d7474c9.png)

# ### Represent possible network paths in a graph
# Once again, **creating every connection** above **for** a **multiple locations** is **not something we would do by hand**. For one thing, the delivery locations would change each day. So the **graph would be created by software**.

# #### Create a class for each location
# I'll store my locations in a class. We'll keep that simple to just a name and an address here.

# In[ ]:


class Location:
    def __init__(self, name, address):
        self.name = name
        self.address = address
       
    def __str__(self):
        return self.name + " (" + self.address + ")"


# #### Create sample locations
# We'll **define a function that creates a list of sample locations**. **In** the ****real world, we can **envision** this as being an **application that generates a list of locations**** for each driver in the morning, **based on** the **scheduled deliveries** we have. In our example, we will simply create a some fake locations with place holder addresses. We'll **add** the **Warehouse to** the **beginning of** the **list**, since that's where we'll start and end our delivery day.

# In[ ]:


def create_locations(number_of_locations):
    '''
    Create random locations to be used in upcoming examples.
    '''

    # create a list, starting with the warehouse location
    delivery_locations = [Location("Warehouse", "123 Main Street")]
    
    # iterate through number of locations and add them to the list
    for i in range(1, number_of_deliveries + 1):
        # create a location name and placeholde address
        location_name = "Loc" + str(i)
        address = str(i) + " Main Street"
        delivery_locations.append(Location(location_name, address))

    # return list of locations
    return delivery_locations


# Now let's create some locations ...

# In[ ]:


# number of delivery locations
number_of_deliveries = 9


# In[ ]:


# create a list, starting with the warehouse location
delivery_locations = create_locations(number_of_deliveries)

# print each location in the list to confirm
for location in delivery_locations:
    print(location)


# #### Create a function to populate a Graph with possible connections
# Now I'll **write code** for a function to **create** a **graph from** a list of locations. **In** a **real scenario**, my **function would** use of many available **geolocation APIs** to **take two addresses and return the driving distance** between them. **In our case**, we'll **use a random number generator** to generate random distances. That's fitting, considering each day the delivery locations would change.

# In[ ]:


import random

def driving_distance(address1, address2):
    '''
    In a real case, this would invoke a geolocation API to get the drivign distance between two
    addresses. For our example, we'll just use a random number generator.
    '''
    return random.randint(2, 15)

def graph_routes(graph, locations):
    '''
    Create a route graph based on a list of locations.
    '''
    # iterate through each location in the list
    for location1 in locations:
        # iterate through each other location in the list
        for location2 in locations:
            # if the two locations are not the same
            if location1 != location2:
                # add edge to the graph with a random distance
                graph.add_edge(location1.name, location2.name, 
                               driving_distance(location1.address, location2.address))


# #### Create the graph for the all the routes
# Now we simply **create** on of our **MyWeightedGraph graphs**, and **use** the **function** above **to populate it with** all the **connections between locations**.

# In[ ]:


# create graph to represent possible routes and distances
delivery_routes_graph = MyWeightedGraph(directed = False)

# populate graph with delivery locations
graph_routes(delivery_routes_graph, delivery_locations)


# ### Visualize the graph
# Once again, we'll quickly visualize the graph as we did earlier.

# #### Basic text output

# In[ ]:


# print text representation of the final graph
delivery_routes_graph.print_graph()


# If we **select a few nodes**, we can **see they represent** the **rule I described**. Look for the "B06" node for instance, and see that it will have the connections we mentioned earlier in our example.

# #### Graphic representation with external library
# Once again, there are **too many connections** to make any observations. **But** our **algorithms are coming up** next ...

# In[ ]:


# display graph with nodes and edges from my SimpleGraph object
#gp.draw_graph(delivery_routes_graph.get_nodes(), delivery_routes_graph.get_edges(), weighted = True)


# And here is the usual screen shot.

# ![networkx6.png](attachment:7a169bf3-c792-4089-8621-d0c2196a7980.png)

# # Algorithms
# I've mentioned a few times that much of the benefit of representing relationships in graphs, is in the ability to derive information through algorithms. We'll look at three examples here, but there are more.

# ## Shortest Path
# The **shortest path problem** is the problem of **finding a path between two nodes** such that the **sum of the weights is minimized**.
# 
# There are multiple well known algorithms for calculating the shortest path. On the eLearning, we looked at two at **Dijkstra's algorithm** and **Bellman–Ford algorithm**. 

# ### Dijkstra's algorithm
# The Dijkstra algorithm **works to find the shortest path from a starting node** by **finding** the **shortest subpaths between each node visited** along the path. It is the fastest algorithm with lowest time complexity. However, it is important to remember that **it does not work** correctly **with negative edge weights**.

# In[ ]:


import sys

# define a constant to represent the maximum weight value
MAX_WEIGHT = sys.maxsize

def shortest_paths(graph, start_node):
    '''
    This method implements Dijkstra's algorithm to find the shortest paths from the 'start_node' to all other graph in the graph.
    It returns a dictionary where the keys are the node names, and the values are tuples containing the shortest weight and 
    the path to that node.
    '''
        
    # Initialize a dictionary to store the paths and weights
    # For each node, the initial weight is set to the maximum weight value, and the path is an empty list.
    path_weights = {node: (MAX_WEIGHT, []) for node in graph.get_nodes()}

    # The weight and path for the 'start_node' are set to 0 and an empty list, respectively.
    path_weights[start_node] = (0, []) 

    # Create a priority queue to store the graph to be visited, along with their current weights.
    # The queue is initialized with the 'start_node' and its weight of 0.
    priority_queue = [(0, start_node)]

    # Loop until the priority queue is empty.
    while priority_queue:
        # Sort the priority queue by weight (in ascending order). 
        # The sort will look at the first element in the tupple by default, and that is the weight
        priority_queue.sort()
        
        # Pop the node with the smallest weight from the queue.
        # The elements are (<weight>,<node>) tuples, so as we pop, we assign the weight and node to distinct variables
        current_weight, current_node = priority_queue.pop(0)  

        # If the current weight is greater than the previously recorded weight for this node, 
        # skip it (as we have already found a shorter path).
        if current_weight > path_weights[current_node][0]:
            continue

        # Explore the neighbors of the current node.
        for neighbor, weight in graph.get_node_edges(current_node):
            # Calculate the weight to the neighbor through the current node.
            weight = current_weight + weight

            # If the new weight is shorter than the previously recorded weight for the neighbor...
            if weight < path_weights[neighbor][0]:
                # Update the weight and path for the neighbor.
                path_weights[neighbor] = (weight, path_weights[current_node][1] + [current_node])
                # Add the neighbor to the priority queue with the new weight.
                priority_queue.append((weight, neighbor))

    # Return the dictionary of shortest weights and paths.
    return path_weights


# ### Example - Calculating the shortest commute
# Let's start with one of the most "classic" uses of shortest path: driving directions. Let's bring the NJ driving directions graph we created earlier, which had various significant cities around my home town of Freehold.

# ![nj_map.png](attachment:de8a5e12-483c-47df-b737-4cd889ea33ef.png)

# #### Reviewing the graph
# Let's **recap** the **graph data previously entered** in the **nj_drive_graph variable**.

# In[ ]:


# print text representation of the final graph
nj_drive_graph.print_graph()


# #### Check shortest driving paths today from a city
# Based on the data I entered, let's **check** the **best driving Paths to all points from** my home town of **Freehold**.

# In[ ]:


# Call method to populate full driving path dictionary
start_city = "Freehold"
best_drives = shortest_paths(nj_drive_graph, start_city)

# iterate through dictionary and print al the paths
print(f"Shortest paths from {start_city}:")
for node, (distance, path) in best_drives.items():
    # exclude drive to start city itself
    if (node != start_city):
        print(f"To {node}: Distance = {distance}, Path = {' -> '.join(path + [node])}")


# This is not **particular interesting**. The **direct paths** were **always the best ones**. That's **not suprising** with **only a few cities**. Remember that **in** a **real driving direction**, **every street intersection is a node**, with the **streets connecting** them being the **edges**. That will give us a lot more options.
# 
# We'll **simulate** the power of the **algorithm** with a fun **example below** ...

# #### Add a city with a "magic portal" from Holmdel to Princeton
# Just for fun, let's **pretend in Holmdel**, where they uncovered the "Big Bank Theory", invented UNIX, and invented the transistor among a lot of things, we have a **secret portal to Princeton**, where Albert Einstein taught. So we'll **add some distances to and from Holmdel**.

# In[ ]:


# Add an edge from Freehold to Holmdel. No magic portal there
nj_drive_graph.add_edge("Freehold", "Holmdel", 15)

# Now add a magical practically instant travel from Holmdel to Princeton
nj_drive_graph.add_edge("Holmdel", "Princeton", 1)

# print updated graph
nj_drive_graph.print_graph()


# #### Recheck the distances
# Notice that **now** our **trip to Priceton will go through Holmdel, even though it's an extra stop**. In fact, a few other paths take advantage of our magic portal.

# In[ ]:


# Call method to generate the shortest paths from the start city
start_city = "Freehold"
best_drives = shortest_paths(nj_drive_graph, start_city)

# iterate through dictionary and print al the paths
print(f"Shortest paths from {start_city}:")
for node, (distance, path) in best_drives.items():
    # exclude drive to start city itself
    if (node != start_city):
        print(f"To {node}: Distance = {distance}, Path = {' -> '.join(path + [node])}")


# ### Example - Calculating indirect social connections
# Driving distances may be one of the more intutive uses of **shortest paths algorithms**, but they **can be applied to less obvious cases**. Often times in **social network**, we want to **see** different **people** that **we have** an **indirect connection to**, and how far removed that is. We'll **bring back** the **social_graph** social network graph we **created early in** this **notebook**.

# #### Reviewing the graph
# Let's **recap** the **graph data previously entered** in the **social_graph variable**.

# In[ ]:


# print text representation of the final graph
social_graph.print_graph()


# And here is the visual graph for it ...

# ![networkx1.png](attachment:e2b239c4-e49d-4b7f-8fcf-42fd57dc68ef.png)

# #### Add default weights to graph
# The social_graph graph had no weights assigned, but the shortest path algorithm expects a weight for each edge. All we need to do is to add a weight of 1 to each edge, and then we can apply the algorithm.
# 
# The MyWeightedGraph class we created has a factory method that allows us to create a weighted graph from an unweighted one, applying a default weight.

# In[ ]:


# create a weighted graph based on social_graph, adding a default weight of 1 to all edges
weighted_social_graph = MyWeightedGraph.create_from_unweighted(social_graph)

weighted_social_graph.print_graph()


# #### Check the direct and undirect connections for a person
# Based on the data I entered, let's **check** the all of the connections for a person.

# In[ ]:


# Call method to generate the shortest paths from the person
person = "mary_major"
social_connections = shortest_paths(weighted_social_graph, person)

# iterate through dictionary and print all direct and indirect connections 
print(f"All connections for {person}:")
for node, (level, connection_path) in social_connections.items():
    # exclude connection from the person themselves
    if (node != person):
        print(f"To {node} ({level}): {' -> '.join(connection_path + [node])}")


# ## Minimum spanning tree
# A **Minimum Spanning Tree (MST)** is a **subset of the edges of a graph** that connects all the node together, **without any cycles** and **with the minimum possible total weight**.
# 
# There are multiple well known algorithms for calculating the minimum spanning tree. On the eLearning, we looked at two at **Prim's algorithm** and **Kruskal’s algorithm**. 

# ### Prim's algorithm
# Prim's algorithm finds the MST by starting at a random node in the graph as the MST (a single node at that point). The algorithm then finds the node with the lowest edge weight from the current MST, and includes that to the MST. Prim's algorithm keeps doing this until all nodes are included in the MST.
# 
# The **implementation** is **quite complex**, and **understand it step by step** is **not as important as understanding how it is used**, which we will see next.

# In[ ]:


def prims_mst_algorithm(graph):
    # Retrieve data from the graph
    # This algorithm relies on a two-dimension adjacency matrix to store all the edges weights
    # it operates with numbered nodes, and maps the data to the numbers in a side structure
    graph_size = graph.size()
    adj_matrix = graph.get_adjacency_matrix()
    vertex_data = graph.map_numbers_to_nodes()

    # initialize a variable to maintain the MST path
    mst_path = []

    # initialize a list to track which nodes are in the MST
    in_mst = [False] * graph_size

    # initialize lists to track the key values and parents of each node
    key_values = [float('inf')] * graph_size
    parents = [-1] * graph_size

    # set the first key value to be the first node
    key_values[0] = 0 

    # iterate through every node
    for _ in range(graph_size):
        # find the node with the minimum key value that is not in the MST
        u = min((v for v in range(graph_size) if not in_mst[v]), key=lambda v: key_values[v])

        # mark the node as being in the MST
        in_mst[u] = True

        # if the node has a parent, add the edge to the MST path
        if parents[u] != -1:
            mst_path.append((vertex_data[parents[u]], vertex_data[u], adj_matrix[u][parents[u]]))
        
        # iterate through all the nodes
        for v in range(graph_size):
            # if the node is not in the MST, the edge is not to itself, and the edge is smaller than the current key value
            if 0 < adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                # update the key value and parent of the node
                key_values[v] = adj_matrix[u][v]
                parents[v] = u
                
    return mst_path


# ### Example - Calculating the optimal wiring for a LAN
# Let's look back at our LAN network from earlier in this Notebook.

# ![graph7.png](attachment:6c39a051-8765-4fe7-ab14-5e4513cdc255.png)

# A **common question** we would ask is **what is the optimal wiring plan** to **connect all these workstations** such that we use the least amount of cables. Essentially, what we are **looking for** then is the **Minimum Spanning Tree** for this graph.

# #### Reviewing the graph
# Let's **recap** the **graph data previously entered** in the **floor_plan_graph variable**.

# In[ ]:


# print text representation of the final graph
floor_plan_graph.print_graph()


# #### Calculating the MST
# Based on that data, we will **use** the **prism algorithm** to **calculate the Minimum Spanning Tree**, which will give us the best wiring.

# In[ ]:


# calculate MST
mst_edges = prims_mst_algorithm(floor_plan_graph)

# sort the edges, so the it's easier to visualize
mst_edges_sorted = sorted(mst_edges)

print("Minimum Spanning Tree (MST) Edges:") 
for edge in mst_edges_sorted: 
    print(edge, end=" ")


# It's not easy to visualize the path looking through that long list, but I saved you time drawing the **lines defined by the edges above on** top of our **floor plan image**:

# ![graph8.png](attachment:53f15010-a9d1-402b-baee-874c2179a39d.png)

# It's not easy to confirm visually that this is the best path, but it looks pretty good to me.

# ## Travelling Salesperson
# The **Travelling Salesperson problem** is states that: *"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?*"
# 
# The **problem can be generalized** to **many use cases** where you are **looking for** the **optimal path around every node, without repeating** any, and **returning to** the **first node**.
# 
# There are **multiple well known solutions** for the travelling salesperson problem. On the eLearning, we **looked at** two at the **brute force method**, **and** the **nearest neighbor** algorithm. The **brute force** method is the **most accurate**, but **not as efficient** for a large number of nodes. **Nearest neighbor** is **not as accurate**, but **performs better**.

# ### The Brute Force Method
# The **brute-force method** ensures that we will calculate the correct answer because it **calculates the distances from each node to every other node**. Then, it **builds all the possible paths from** the **starting node to** visit **every other node**. It works well with small datasets, but it's very time consuming to run when the number of nodes increases. 
# 
# Again, the **implementation** is **quite complex**, and **understand it step by step** is **not as important as understanding how it is used**, which we will see next.

# In[ ]:


def generate_permutations(arr):
    '''
    This helper function generates all permutations of a given list.
    '''
    # checks for an empty array
    if not arr:
        return [[]]

    # initialize an empty list to store the permutations
    permutations = []

    # iterate through the array and generate all the combinations
    for i in range(len(arr)):
        remaining = arr[:i] + arr[i + 1:]
        for p in generate_permutations(remaining):
            permutations.append([arr[i]] + p)

    return permutations

def solve_tsp(graph):
    '''
    This function solves the traveling salesman problem using brute force.
    It takes a graph as input and returns the shortest path and its distance.
    '''

    # set the graph size
    graph_size = graph.size()

    # get the adjacency matrix from the graph
    adjacency_matrix = graph.get_adjacency_matrix()
    
    # Generate all possible permutations of nodes
    node_paths = generate_permutations(list(range(graph_size)))

    # Initialize variables to store the optimal path and total distance
    optimal_path = None
    min_distance = float('inf')

    # Iterate through all permutations and calculate the total distance
    for path in node_paths:
        distance = 0
        for i in range(graph_size - 1):
            # get the distance between consecutive nodes in the path, and add it to the total distance
            distance += adjacency_matrix[path[i]][path[i + 1]]
        # Add the distance from the last node to the starting node
        distance += adjacency_matrix[path[-1]][path[0]]

        # Update optimal tour if current permutation is shorter distance
        if distance < min_distance:
            min_distance = distance
            optimal_path = path

    # convert path to node names
    map_numbers_to_nodes = graph.map_numbers_to_nodes()
    optimal_path_names = [map_numbers_to_nodes[node_idx] for node_idx in optimal_path]

    return optimal_path_names, min_distance


# ### Example - Calculating the optimal delivery route
# Let's **return to** the **problem we setup before**, where we needed to **optimize truck delivery routes**. We have a **driver** that **leaves a warehouse** in the morning, and must **make deliveries to multiple locations** before returning to the warehouse. 
# 
# We **already saw** how we **represent every possible route** **using** a **graph**. I'll **repeat the same steps we saw earlier below**, so we can see everything together without scrolling up.

# #### Create sample locations
# Using the functions we had created earlier, we'll **create one location for** the **warehouse**, **plus** a **number of locations**and **put all the locations in a list**.

# In[ ]:


# number of delivery locations
number_of_deliveries = 5


# In[ ]:


# create a list, starting with the warehouse location
delivery_locations = create_locations(number_of_deliveries)

# print each location in the list to confirm
for location in delivery_locations:
    print(location)


# #### Use a function to populate a Graph with possible connections
# **Earlier we defined** the ***graph_routes*** **function**, which **creates a graph** with **simulated distances between** the **locations provided**.  The function **uses a random number generator** to generate random distances.

# In[ ]:


# create graph to represent possible routes and distances
delivery_routes_graph = MyWeightedGraph(directed = False)

# populate graph with delivery locations
graph_routes(delivery_routes_graph, delivery_locations)


# #### View the graph
# Let's **view** the **graph data we created**.

# In[ ]:


# print text representation of the final graph
delivery_routes_graph.print_graph()


# We can also **view each edge with** the**weight** between them ...

# In[ ]:


# print text representation of the final graph
delivery_routes_graph.print_edges()


# #### Graphic representation with external library
# We can draw a quick graph to visualize ...

# In[ ]:


# display graph with nodes and edges from my SimpleGraph object
#gp.draw_graph(delivery_routes_graph.get_nodes(), delivery_routes_graph.get_edges(), weighted = True)


# I'll **add a screenshot** here just so you can view the shape, **but remember** that the **distances are randomly generated** each time, so they'll **not match the text** printout.

# ![networkx7.png](attachment:36bcfe29-3be4-4f9e-abb3-5156ca340c71.png)

# #### Calculating the optimum delivery path
# Based on that data, we will **use** the **travelling salesperson algorithm** to **calculate the optimum delivery path**.

# In[ ]:


# calculate MST
optimal_path, total_distance = solve_tsp(delivery_routes_graph)

print("Optimal delivery path:") 
for edge in optimal_path: 
    print(edge, end=" --> ")
print(optimal_path[0])

# print the total distance
print(f"Total distance: {total_distance} miles")


# #### Repeat the process with new distances
# Let's **repeat** the **process** above, which will **generate new random distances**. **Will** the optimal **route change?**
# 
# I'm **calling** the **same functions**, but I will **not break down step by step**.

# In[ ]:


# number of delivery locations
number_of_deliveries = 4

# create a list, starting with the warehouse location
delivery_locations = create_locations(number_of_deliveries)

# create graph to represent possible routes and distances
delivery_routes_graph = MyWeightedGraph(directed = False)

# populate graph with delivery locations
graph_routes(delivery_routes_graph, delivery_locations)

# calculate MST
optimal_path, total_distance = solve_tsp(delivery_routes_graph)

print("Optimal delivery path:") 
for edge in optimal_path: 
    print(edge, end=" --> ")
print(optimal_path[0])

# print the total distance
print(f"Total distance: {total_distance} miles")


# **Did you see a new route? You should have**. You can run the call a few more times and verify.
# 
# Again, that would be the **equivalent of a driver getting custom delivery routes each morning**, based on the deliveries for that day.

# #### Calculating the optimum delivery path for more locations
# Now let's **repeat** the **process** above, but this time we'll **increase** it to **10 locations** (warehouse, plus 9 deliveries).

# In[ ]:


# number of delivery locations
number_of_deliveries = 9

# create a list, starting with the warehouse location
delivery_locations = create_locations(number_of_deliveries)

# create graph to represent possible routes and distances
delivery_routes_graph = MyWeightedGraph(directed = False)

# populate graph with delivery locations
graph_routes(delivery_routes_graph, delivery_locations)

# calculate MST
optimal_path, total_distance = solve_tsp(delivery_routes_graph)

print("Optimal delivery path:") 
for edge in optimal_path: 
    print(edge, end=" --> ")
print(optimal_path[0])

# print the total distance
print(f"Total distance: {total_distance} miles")


# #### Observations
# Did you **notice how that was a lot slower?** The **brute force method** is accurate, but **does not scale very well**. It's an example of an **algorithm with factorial order of magnitute (O(n!))**, which is about as bad as it gets when it comes to scaling. That's a topic we'll discuss in the future.
# 
# **For an approximation** of the best route **with a better performance**, the **nearest neighbor algorithm** might be a better choice.
