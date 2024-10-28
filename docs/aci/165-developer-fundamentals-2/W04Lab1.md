# Finding the Shortest Path with Directed and Undirected Graphs

## Lab overview

In this lab, you use both directed and undirected graphs to solve the shortest paths problem.

Objectives
By the end of this lab, you should be able to do the following:

Work with graph structures.
Build a graph structure and fill it with data.
Implement Dijkstra’s algorithm to find the shortest route.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, macOS X, or Linux (Ubuntu, SUSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Duration
This lab requires approximately 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance. Additional information or elaboration on a point
 Hint: A hint to a question or challenge
 Task complete: A conclusion or summary point in the lab
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Task 1: Complete the UGraph library and print a graph
In this task, you will complete the code for the UGraph class and functions. Then, you will use Ugraph to print a sample graph. UGraph is used to create and print undirected graph objects. Undirected graphs are graphs with edges that can be traveled in both directions.

Task 1.1 Finish the add_edge function
First, you will complete the Ugraph class by finishing the add_edge method. The add_edge method will create edges using three parameters, from_node (start node), to_node (end node), and distance.

In the left navigation pane of the lab instructions, under Resources, copy and paste the Cloud9Environment URL into a new browser tab to open the AWS Cloud9 environment.

In the left navigation pane of the AWS Cloud9 IDE, open the ugraph.py file.

Review the ugraph.py code and comments.

To review ugraph.py here, expand this section.
 Consider: In the __main__ section of ugraph.py, code has been written to represent the undirected graph in the following diagram, however the add_edge function does not include statements which create edges.

An undirected graph with four nodes (X, A, B, and C) and five edges.

Image description: An undirected graph with four nodes and five edges. The nodes are represented by the letters X, A, B, and C. The edges of the undirected graph are represented using lines with arrows at both ends. The distance between nodes X and A is 7. The distance between nodes A and B is 3. The distance between nodes B and C is 2. The distance between nodes X and C is 1. The distance between nodes X and B is 2.

In the ugraph.py file, within the add_edge function, add statements which define a new edge and its distance in the graph.
 Note: Remember that each edge has two directions. The add_edge function should complete the following steps:

Add an entry in the edges dict for the from_node to the to_node.
Add an entry in the edges dict for the to_node to the from_node.
Add an entry in distances dict to represent the distance from the from_node to the to_node.
Add an entry in distances dict to represent the distance from the to_node to the from_node.
If you are not sure what to use for the key and value, check the comments in the __init__ constructor.

For an example of the completed solution, expand this section.
Task 1.2: Print the graph created using Ugraph
Now that you have completed the add_edge function in the Ugraph class, you will print the undirected graph defined in the __main__ function of ugraph.py.

At the top of the AWS Cloud9 IDE, choose Run to run ugraph.py.
 Expected output:


X: A(7), B(2), C(1)
A: X(7), B(3) 
B: X(2), A(3), C(2) 
C: B(2), X(1)
 Note: The output represents the information in the graph. Node X has an edge connecting to node A with distance 7. Node X has an edge connecting to node B with a distance of 2. Node X has an edge connecting to node C with a distance of 1.

 Task complete: You have completed the UGraph class by adding code to the add_edge function, and printed a graph.

Task 2: Define a graph and use Dijkstra’s algorithm to find the shortest path between nodes
Dijkstra’s algorithm finds the shortest path between two nodes. It does this by visiting each node one time and finding the shortest path from that node to the starting node. It successively builds a subpath graph containing the shortest paths from the starting node to each node in the tree.

In this task, you will modify a file that includes an implementation of Dijkstra’s algorithm by defining a graph using the Ugraph class created in the previous task. Then you run the updated file to find the shortest path between the nodes.

Task 2.1: Define a graph
First, you will modify the __main__ function in dijkstra.py to define a graph.

In the left navigation pane of the AWS Cloud9 IDE, open the the dijkstra.py file.

Review the dijkstra.py code and comments.

To review dijkstra.py here, open this section.
 Consider: The first lines of dijkstra.py import the Ugraph class that was completed in the previous task. This allows the Ugraph class and its functions to be called within dijkstra.py.

In the dijkstra.py file, within the __main__ function, include add_edge calls from the Ugraph class that define edges and distances which match the graph illustrated below.
An undirected graph with four nodes (A, B, C, and D) and five edges.

Image description: An undirected graph with four nodes and five edges. The nodes are represented by the letters A, B, C, and D. The edges of the undirected graph are represented using lines with arrows at both ends. The distance between nodes A and B is 1. The distance between nodes B and D is 5. The distance between nodes D and C is 1. The distance between nodes A and C is 4. The distance between nodes B and C is 2.

For an example of the completed solution, expand this section.
Task 2.2: Run the dijkstra.py to find the shortest paths between nodes
Now that the graph is defined within the __main__ function of dijkstra.py, you will run dijkstra.py to review the shortest paths between nodes.

At the top of the AWS Cloud9 IDE, choose Run to run dijkstra.py.
 Expected output:


(['A', 'B', 'C', 'D'], 4)
(['B', 'C', 'D'], 3)
(['C', 'B'], 2)
(['D', 'C', 'B'], 3)
 Task complete: You have defined a graph and used Dijkstra’s algorithm to find the shortest path between specified nodes.

Task 3: Find the shortest path for your errands
With a graph structure and Dijkstra’s algorithm prepared, you can now search for the shortest paths to your destinations. In this task, the graph is already defined. The route is: Home (H) -> Pharmacy (P) -> Gym (G) -> Shop (S). Find the shortest route between locations.

Open the shortest_path.py file.

Write code that finds the shortest route between “H->P”, “P->G”, and “G->S”.

 Hint: In the __main__ function of shortest_path.py, write a loop that displays the shortest path between each of the nodes in the route. The desired route is stored in the tuple route. You might first want to write the code that prints the pairs of destinations in the route. For example, print “H P”, “P G”, “G S”.

An undirected graph with 6 nodes and 15 edges.

Image description: An undirected graph with 6 nodes and 15 edges. The nodes are represented by the letters H, G, P, R, S, and W. The edges of the undirected graph are represented using lines with arrows at both ends. The distance between nodes H and P is 3. The distance between nodes H and S is 5. The distance between nodes H and W is 2. The distance between nodes H and G is 1. The distance between nodes H and R is 10. The distance between nodes P and S is 4. The distance between nodes P and W is 3. The distance between nodes P and G is 5. The distance between nodes P and R is 6. The distance between nodes S and W is 7. The distance between nodes S and G is 9. The distance between nodes S and R is 3. The distance between nodes W and G is 3. The distance between nodes W and R is 8. The distance between nodes G and R is 7.

For an example of the completed solution, expand this section.
 Expected output:


(['H', 'P'], 3)
(['P', 'H', 'G'], 4)
(['G', 'H', 'S'], 6)
 Task complete: You have used Dijkstra’s algorithm to find the shortest routes for your destinations.

Task 4: Upgrade the solution to consider one-way streets (Optional)
In real life, you sometimes take one-way streets to get to your destination. In this task, you expand the solution to support one-way streets.

Task 4.1: Create the DGraph class
In this task, you create a DGraph class to represent a directed graph.

Create a new file called dgraph.py.

Write code to implement an undirected graph.

 Hint: The directed graph class is nearly identical to the undirected graph class, except the add_edge function does not add edges in both directions. Call the new class DGraph.

In the main section of the DGraph class, add code to represent the nodes and edges as depicted in the following diagram.
A directed graph with four nodes (X, A, B, and C) and five edges.

Image description: A directed graph with four nodes and five edges. The nodes are represented by the letters X, A, B, and C. The edges of the directed graph are represented using lines with an arrow at one end indicating direction from the first node to the second node. The distance from node X to node A is 7. The distance from node A to node B is 3. The distance from node B to node C is 2. The distance from node C to node X is 1. The distance from node X to node B is 2.

Run the program by choosing the Run button at the top of the page.
 Expected output:


X: A(7), B(2)
A: B(3)
B: C(2)
C: X(1)
For an example of the completed solution, expand this section.
 Note: The input edges are the same for both UGraph and DGraph. But the graph structure is different because of the directionality.

Add new edges so that you get the same result as in Task 1. The edges do not have to be in the same order, but each vertex must have the same edges of the same length.

Run the program by choosing the Run button at the top of the page.

 Expected output:


X: A(7), B(2), C(1) 
A: X(7), B(3) 
B: X(2), A(3), C(2) 
C: B(2), X(1)
For an example of the completed solution, expand this section.
 Task complete: You have successfully implemented the DGraph class.

Task 4.2: Use Dijkstra’s algorithm to navigate the directed graph
In this task, you implement the shortest path algorithm using a directed graph.

Return to the shortest_path.py file, and modify it to use DGraph instead of UGraph.

Run the program by choosing the Run button at the top of the page.

 Expected output:


(['H', 'P'], 3)
(['P', 'G'], 5)
Traceback (most recent call last):
  File "/home/ubuntu/environment/solution/shortest_path_task4.py", line 36, in <module>
    print(find_shortest_path(graph, route[i], route[i+1]))
  File "/home/ubuntu/environment/solution/dijkstra.py", line 37, in find_shortest_path
    raise Exception("Route not possible")
Exception: Route not possible
 Note: The route through the graph is not possible because one of the edges is missing.

For an example of the completed solution, expand this section.
Find the missing path and add it to the distances variable.
 Hint: In the distances variable, a path is missing that goes from node G to node P. Reference the diagram in Task 3 to find the edge from node G to node P.

Run the program by choosing the Run button at the top of the page.
 Expected output:


(['H', 'P'], 3)
(['P', 'G'], 5)
(['G', 'P', 'S'], 9)
For an example of the completed solution, expand this section.
 Task complete: You have implemented a directed graph and found the shortest path using Dijkstra’s algorithm.

Conclusion
You have successfully done the following:

Worked with graph structures
Built a graph structure and filled it with data
Implemented Dijkstra’s algorithm to find the shortest route
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.