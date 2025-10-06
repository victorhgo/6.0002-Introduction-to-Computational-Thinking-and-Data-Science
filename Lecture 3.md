# Lecture 3 - Graph-theoretic Models

In this lecture, we will be exposed to the idea of graph models and depth-first and breadth-first search algorithms.

## Content

- [What is a graph](#what-is-a-graph?)
- [The usefulness of graphs](#the-usefulness-of-graphs)
- [Implementing and using Graphs](#implementing-and-using-graphs)
- [Common Representation of Diagraphs](#common-representation-of-diagraphs)
- [Search on a Graph](#search-on-a-graph)
- [Navigation problem: Getting from a City to Another](#navigation-problem-getting-from-a-city-to-another)
- [Building the Graph for Cities](#building-the-graph-for-navigation-problem)
- [Depth First Search - DFS](#depth-first-search-dfs)
- [Breadth First Search - BFS](#breadth-first-search---bfs)
- [Weighted Edges for Graphs and Digraphs](#weighted-edges-for-graphs-and-digraphs)
- [Considerations](#considerations)

## What is a graph?

A graph has two elements: a set of nodes (also known as vertices) where these nodes probably are going to have information (data) associated to them, these values can be a name, a value, or a student record for instance. And we also have edges (also known as arcs), which connects a pair of nodes. We use graph to understand what are the connection between the nodes.

We can build graphs in two ways using edges:

1. The simpler one, is an edge that's going to be *undirected* (graph)

An edge connects two nodes together and allows information sharing between both nodes.

For some cases, we are going to use a **directed graph**, also know as *diagraph*

2. Directed (diagraph)

In this case, the edges have a direction from a *source* (parent) and *destination* (child) nodes, thus the information can only flow **from the source to the child**

The edges can be just connections, but in some cases we're going to put information on them, for instance: weight, where it's going to show us how much effort will take to go from a source to a destination. 

We think on how can we pass through this graph, finding a path from one place to another: for instance, minimizing the cost associated with passing through the edges? Or how can we find a connection between two nodes in the graph?

### The usefulness of graphs

Why do we want to use graphs? Well, suppose we take a vacation to Europe and we want to check what are the possible ways **by rail** can I get from Paris to London? We can think of it as a graph, where the nodes are cities and the railroads are links between them. First question: can we get from Paris to London? If yes, what's the **fastest** way to do it? (Or the cheapest one).

Another application for graphs is modeling of complex molecule of the relationships between the pieces inside of it and we can ask: what kind of energy would it take to convert this molecule into a different one? An application on drug discovery.

Another application is family tree (or ancestral relationships). In most families they are trees and not graphs, but family trees are a demonstration of relationships because there are directional edges: parent have children, those children have children. And also, **trees are a special case of a graph**, as we used decision trees.

The property of a tree: any pair of nodes are connected, and if they are connected it's only by a single path. There are no ways to go from one node, find a set of things that brings we back to that node, thus there only a single path to those points. Australian trees start in the root (top), and the leaves are at the bottom. 

**The world is full of networks that are based on relationships that could be captured by a graph:**

- Computer Networks: sending an email from a machine to another. The network is set up by a series of routers that pass it along. Sending something requires an algorithm that figures out the best way to actually move it around.

- Transportation Networks: Make the nodes cities and edges roads between them and ponder questions.

- Financial Network: Moving money around

- Traditional Network: Electric, Water, anything that distributes content. How can we maximize distribution of water in an appropriate way given the certain capacities on different pipes, which means those edges in the graph will have different weights.

- Political Network, Criminal Networks, Social Networks...

Graphs can capture interesting relationships in connected networks of elements. But they can also support inferences on these structures such as:

- Finding sequences of links between elements: is there a path from A to B?

- Finding the least expensive path between elements (or the shortest path problem)

- Partitioning the graph into sets of connected elements (graph partition problem)

- Finding the most efficient way to separate sets of connected elements (min-cut/max-flow problem)

Navigation applications nowadays uses graph theory where they model road systems using a diagraph such that nodes are points where roads end or meet and the edges are connections between points. Each edge has a weight (expected time to get from A to B for a edge, distance between A and B nodes and average speed of travel between A and B nodes)

We solve this optimization problem by finding the shortest weighted path between A and B.

First reported use of Graph Theory: Bridges of Königsberg solved by Leonhard Euler

## Implementing and using Graphs

**Building a graph:** We require Nodes, Edges and we stitch them together to make graphs, let's start by building a Node class:

```py
class Node(object):
    def __init__(self, name):
        """ Assumes Node's name is a string """
        self.name = name

    # Get method
    def getName(self):
        return self.name

    def __str__(self):
        return self.name
```

Now we can build a class Edge, where we associate the Source and Destination for this Edge.

```py
class Edge(object):
    def __init__(self, source, destiny):
        """ Assumes Source and Destiny are Nodes """
        self.source = source
        self.destiny = destiny

    # Get methods
    def getSource(self):
        return self.source

    def getDestination(self)
        return self.destiny
    
    def __str__(self):
        return self.source.getName() + '->'\
            + self.destiny.getName()
```

How to make decision about the graph? We can start by diagraphs (directed graphs) and we need to define how we will represent the graph. We can create nodes and edges, but we need to bring them all together to build a graph. 

### Common Representation of Diagraphs

Since a diagraph is a directed graph where edges pass in one direction only, we can use an adjacency matrix where rows are the source nodes and columns are the destination nodes, and Cell[s,d] = 1 if there is an edge from s to d, or 0 otherwise. But for diagraph, the matrix is not symmetric.

We can also have an **adjacency list**, where we associate each node a list of destination nodes.

Let's build a class ```Diagraph``` where we will map each node to a list of its children.

```py
class Diagraph(object):
    def __init__(self):
        """ Edges is a dictionary mapping each node to a list of its children """
        self.edges = {}

    def addNode(self, node):
        """ Nodes are represented as keys in dictionary """
        if node in self.edges:
            raise ValueError('Node already exists!')
        else:
            self.edges[node] = []
    
    def addEdge(self, edge):
        """ Edges are represented by destinations as values in list associated with a source key"""
        source = edge.getSource()
        destiny = edge.getDestination()
        
        if not (source in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        
        self.edges[source].append(destiny)
    
    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for node in self.edges:

            if node.getName() == name:
                return node

        # Only raise error if name not found        
        raise NameError(name)

    def __str__(self):
        result = ''

        for source in self.edges:
            for destiny in self.edges[source]:
                result = result + source.getName() + ' -> '\
                    + destiny.getName() + '\n'
        
        # Omit final newline
        return result[:-1]
```

But suppose we want to actually build a Graph, we can do that by making it a subclass of `Diagraph`, the only thing required is to shadow the `addEdge` method from diagraphs. In this way, if we want to build a Graph, it only uses this version of `addEdge` instead of the one from Diagraph. In a  `Graph`, both directions can work, so:

```py
class Graph(Diagraph):
    def addEdge(self, edge):

        Diagraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())

        Diagraph.addEdge(self, rev)
```

> But why ```Graph``` is a subclass of `Diagraph` and not the other way around? Because anything that works for a Diagraph will also work for a Graph. Therefore it's easier to make the Graph a subclass of Diagraph.

## Search on a Graph

A classic Graph optimization problem is to find the best path. In the following example let's find the best path home, in other words, what's the shortest path from one node to another?

> In this example, the **shortest path** initially will just be the **shortest sequence of steps** to go from one Node to another.

The **shortest path** with the property that the source of the first edge is the starting point and the destination of the last edge is the thing we're trying to get to (a city for instance, as we will see on further example).

For any edge in between, if we go in our first edge from source to `Node 1` for instance, the next edge has that destination as its source. It's a simple chain that says we can go from here to here all the way through.

If those edges have `weights` on them (distance, for instance), then the optimization problem we are trying to solve will be shortest weighted path (shortest distance).

Examples of **finding the shortest path problem** includes:

- Finding a navigation route, designing communication networks, lots of biological problems.

### Navigation problem: Getting from a City to Another

Given a set of cities, we can think of flight paths between them:

**Adjacency list:** (From the given city, we can get to the following cities)

- Boston: Providence, New York
- Providence: Boston, New York
- New York: Chicago
- Chicago: Denver, Phoenix
- Denver: Phoenix, New York
- Lost Angeles: Boston
- Phoenix: (Phoenix has no exits out of it)

These will be the *keys* in the dictionary (the nodes) and each one of the lists is a set of Edges from the source to the destination.

#### Building the Graph for Navigation Problem:

Let's create the previous adjacency list:

```py
def buildCityGraph(graphType):
    g = graphType()
    
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): # Creates 7 cities nodes
        g.addNode(Node(name))

    # Associates each node to edges    
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))

    return g
```

To find the shortest path, the first technique we'll use is **Depth First Search (DFS)**

### Depth First Search (DFS)

Depth First Search it's similar on the knapsack problem when we took the left most depth first method of the search tree. But since we're using Graph and not Tree, there are potential for loops, thus we need to keep track of what's in the path and never going back to a node that's already in the path. In other words, we'll never visit a city that we've already visited.

We can also take advantage of divide and conquer. If we want to find a path from a source node to a destination node, if we can find a path to some *intermediate* node from **source intermediate** and then find a path from **intermediate to destination**, the combination is a entire way path. We can break this down into simpler versions of that search problem **recursively**.

**Depth First Search**

Start off with that source node (initial node) then look all the edges that leave that node in some order. We will follow the first edge and check to see if we're at the right location. If we are in the right location, we're done. If not, the we'll follow the first edge out that node. Note that we are creating a loop in this step:

- Start at an initial Node

- Consider all the edges that leaves that node, in some order

- Follow the first edge and check to see if at goal node

- If not, repeat the process from new node

- Continue until either find goal node, or run out of option
    - If run out of options, backtrack to the previous node and try the next edge, repeating the process.

```py
def DFS(graph, start, end, path, shortest, toPrint = False):
    """ 
    Assumes: Graph is a Diagraph;
        start and end are nodes;
        path and shortest are lists of nodes;
    
    Returns: shortest path from start to end in graph
    """
    path = path + [start]

    if toPrint:
        print('Current DFS path:', printPath(path))

    # Base case
    if start == end:
        return path
    
    # Recursive call
    for node in graph.childrenOf(start):
        if node not in path: # To avoid loops
            if shortest == None or len(path) < len(shortest):

                newPath = DFS(graph, node, end, path, shortest, toPrint)

                if newPath != None:
                    shortest = newPath
        
        elif toPrint:
            print('Already visited ', node)
    
    return shortest

def shortestPath(graph, start, end, toPrint = False):
    """ 
    Assumes: graph is a Diagraph;
        start and end are nodes
    Returns: shortest path from start to end in a graph
    """
    return DFS(graph, start, end, [], None, toPrint)
```

We give the DFS a graph, a start node, an end node and a path that got us to that start node. Initially it's going to be an empty list, that tells us what's the shortest path we've found so far.

Since path is an empty list, we give it at the first round the node we're at with `path = path + [start]`. Then we print it some stuff to check where we are. If we are in the destination, we stay there, if not, then we will loop thru all the children of the start node, the nodes we can reach with a single edge. 

Let's pick the first one, then check if it's not in the path to avoid loops, if it's not and assuming we don't have a solution or the best solution is smaller than what we've traveled so far, the algorithm will do the same search.

Now we can create a simple test function and perform some tests:

```py
def testShortestPath(source, destination):
    g = buildCityGraph(Diagraph)

    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print(f'Shortest path from {source} to {destination} is {printPath(sp)}.\n')

    else:
        print(f"There's no path from {source} to {destination}!\n")

if __name__ == '__main__':

    # Testing shortest path from Chicago to Boston
    print("Testing shortest path from Chicago to Boston...")
    testShortestPath('Chicago', 'Boston')
    print('\n')

    # Testing Shortest Path from Boston to Phoenix
    print("Testing the shortest path from Boston to Phoenix...")
    testShortestPath('Boston','Phoenix')
    print('\n')

    # Testing Shortest Path from New York to Denver
    print('Testing the shortest path from New York to Denver')
    testShortestPath('New York', 'Denver')
    print('\n')
```

Running the above test:

```sh
$ py cities.py

    Testing shortest path from Chicago to Boston...
    Current DFS path: Chicago
    Current DFS path: Chicago -> Denver
    Current DFS path: Chicago -> Denver -> Phoenix
    Current DFS path: Chicago -> Denver -> New York
    Already visited  Chicago
    Current DFS path: Chicago -> Phoenix
    There's no path from Chicago to Boston!

    Testing the shortest path from Boston to Phoenix...
    Current DFS path: Boston
    Current DFS path: Boston -> Providence
    Already visited  Boston
    Current DFS path: Boston -> Providence -> New York
    Current DFS path: Boston -> Providence -> New York -> Chicago
    Current DFS path: Boston -> Providence -> New York -> Chicago -> Denver
    Current DFS path: Boston -> Providence -> New York -> Chicago -> Denver -> Phoenix
    Already visited  New York
    Current DFS path: Boston -> Providence -> New York -> Chicago -> Phoenix
    Current DFS path: Boston -> New York
    Current DFS path: Boston -> New York -> Chicago
    Current DFS path: Boston -> New York -> Chicago -> Denver
    Current DFS path: Boston -> New York -> Chicago -> Denver -> Phoenix
    Already visited  New York
    Current DFS path: Boston -> New York -> Chicago -> Phoenix
    Shortest path from Boston to Phoenix is Boston -> New York -> Chicago -> Phoenix.

    Testing the shortest path from New York to Denver
    Current DFS path: New York
    Current DFS path: New York -> Chicago
    Current DFS path: New York -> Chicago -> Denver
    Current DFS path: New York -> Chicago -> Phoenix
    Shortest path from New York to Denver is New York -> Chicago -> Denver.
```

### Breadth First Search - BFS

The idea is similar to DFS, but in BFS the logic it follows is:

- Start at an initial node

- Consider **all the edges** that leave that node, in some order (where we store in Queues)

- Follow the first edge, checking to see if we are at the goal node

- If not, try the next edge from the current node

- Continue until either find the goal node, or run out of options

    - When run out of edge options, move to the next node at same distance from start and repeat again

    - When run out of node options, move to the next level in the graph, where it will be all nodes one step further from start, and repeat

Implementing the algorithm:

```py
def BFS(graph, start, end, toPrint = False):
    """ 
    Assumes: graph is a diagraph
             Start and end are nodes
    Returns: Shortest path from start to end in graph
    """
    initPath = [start]
    pathQueue = [initPath]

    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue

        if printQueue:
            print(f"Queue: {len(pathQueue)}")

            for p in pathQueue:
                print(printPath(p))

        tmpPath = pathQueue.pop(0) # Temporary path removing the oldest element from queue

        if toPrint:
            print(f"Current BFS path: {printPath(tmpPath)}")
            print()
        
        lastNode = tmpPath[-1]

        if lastNode == end:
            return tmpPath

        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)      

    return None  

def shortestPathBFS(graph, start, end, toPrint = False):
    """ 
    Assumes: graph is a Diagraph;
             start, end are nodes

    Returns: Shortest path from start to end in Graph
    """
    return BFS(graph, start, end, toPrint)
```

We can also write a test for BFS in a similar way as we did to the DFS:

```py
def testShortestPathBFS(source, destination):
    g = buildCityGraph(Diagraph)

    sp = shortestPathBFS(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print(f'Shortest path from {source} to {destination} is {printPath(sp)}.\n')

    else:
        print(f"There's no path from {source} to {destination}!\n")

if __name__ == '__main__':

    # Testing shortest path from Chicago to Boston
    print("Testing shortest path from Chicago to Boston...")
    testShortestPathBFS('Chicago', 'Boston')
    print('\n')

    # Testing Shortest Path from Boston to Phoenix
    print("Testing the shortest path from Boston to Phoenix...")
    testShortestPathBFS('Boston','Phoenix')
    print('\n')

    # Testing Shortest Path from New York to Denver
    print('Testing the shortest path from New York to Denver')
    testShortestPathBFS('New York', 'Denver')
    print('\n')
```

Running the above test we get the following output:

```sh
$ py cities.py

    Testing shortest path from Chicago to Boston...
    Queue: 1
    Chicago
    Current BFS path: Chicago

    Queue: 2
    Chicago -> Denver
    Chicago -> Phoenix
    Current BFS path: Chicago -> Denver

    Queue: 3
    Chicago -> Phoenix
    Chicago -> Denver -> Phoenix
    Chicago -> Denver -> New York
    Current BFS path: Chicago -> Phoenix

    Queue: 2
    Chicago -> Denver -> Phoenix
    Chicago -> Denver -> New York
    Current BFS path: Chicago -> Denver -> Phoenix

    Queue: 1
    Chicago -> Denver -> New York
    Current BFS path: Chicago -> Denver -> New York

    There's no path from Chicago to Boston!

    Testing the shortest path from Boston to Phoenix...
    Queue: 1
    Boston
    Current BFS path: Boston

    Queue: 2
    Boston -> Providence
    Boston -> New York
    Current BFS path: Boston -> Providence

    Queue: 2
    Boston -> New York
    Boston -> Providence -> New York
    Current BFS path: Boston -> New York

    Queue: 2
    Boston -> Providence -> New York
    Boston -> New York -> Chicago
    Current BFS path: Boston -> Providence -> New York

    Queue: 2
    Boston -> New York -> Chicago
    Boston -> Providence -> New York -> Chicago
    Current BFS path: Boston -> New York -> Chicago

    Queue: 3
    Boston -> Providence -> New York -> Chicago
    Boston -> New York -> Chicago -> Denver
    Boston -> New York -> Chicago -> Phoenix
    Current BFS path: Boston -> Providence -> New York -> Chicago

    Queue: 4
    Boston -> New York -> Chicago -> Denver
    Boston -> New York -> Chicago -> Phoenix
    Boston -> Providence -> New York -> Chicago -> Denver
    Boston -> Providence -> New York -> Chicago -> Phoenix
    Current BFS path: Boston -> New York -> Chicago -> Denver

    Queue: 4
    Boston -> New York -> Chicago -> Phoenix
    Boston -> Providence -> New York -> Chicago -> Denver
    Boston -> Providence -> New York -> Chicago -> Phoenix
    Boston -> New York -> Chicago -> Denver -> Phoenix
    Current BFS path: Boston -> New York -> Chicago -> Phoenix

    Shortest path from Boston to Phoenix is Boston -> New York -> Chicago -> Phoenix.

    Testing the shortest path from New York to Denver
    Queue: 1
    New York
    Current BFS path: New York

    Queue: 1
    New York -> Chicago
    Current BFS path: New York -> Chicago

    Queue: 2
    New York -> Chicago -> Denver
    New York -> Chicago -> Phoenix
    Current BFS path: New York -> Chicago -> Denver

    Shortest path from New York to Denver is New York -> Chicago -> Denver.
```

### Weighted Edges for Graphs and Digraphs




## Considerations

With DFS, we're always following the next available edge until we get stuck and do the backtrack while in BFS we are always exploring the next equal length option, keeping track in that queue of the things we have left to check.

Introduced a new model: Graphs, which are a great way of representing networks, collection of entities with relationships between them. We have a lot of graph optimization problems, and we were introduced two examples of that.

