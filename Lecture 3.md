# Lecture 3 - Graph-theoretic Models

In this lecture, we will be exposed to the idea of graph models and depth-first and breadth-first search algorithms.

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

**Building a graph** we need Nodes, Edges and we stitch them together to make graphs, let's start by building a Node class:

```py
class Node(object):
    def __init__(self, name):
        """ Assumes name is a string """
        self.name = name
    # Get method
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
```

Now we can build a class Edge:

```py
class Edge(object):
    def __init__(self, source, destiny):
        """ Assumes source and destiny are Nodes """
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

Let's build a class Diagraph where we map each node to a list of its children.

```py
class Diagraph(object):
    """ Edges is a dictionary mapping each node to a list of its children """
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        """ Nodes are represented as keys in dictionary """
        if node in self.edges:
            raise ValueError('Duplicated Node')
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
                result = result + source.getName() + '->'\
                    + destiny.getName() + '\n'
        
        # Omit final newline
        return result[:-1]
```

And finally we can build a class Graph:

```py
class Graph(Diagraph):
    def addEdge(self, edge):
        Diagraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())

        Diagraph.addEdge(self, rev)
```

Why graph is a subclass of diagraph? 28:37


