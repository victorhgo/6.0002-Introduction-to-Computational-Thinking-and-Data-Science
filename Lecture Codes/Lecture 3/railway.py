class Node(object):
    def __init__(self, name):
        """ Assumes name is a string """
        self.name = name

    # Get method
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name

# Edge connects up two nodes
class Edge(object):
    def __init__(self, source, destiny):
        """ Assumes source and destiny are Nodes """
        self.source = source
        self.destiny = destiny

    # Get methods
    def getSource(self):
        return self.source
    
    def getDestination(self):
        return self.destiny
    
    def __str__(self):
        return self.source.getName() + '->'\
            + self.destiny.getName()
    
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
        
        if not (source in self.edges and destiny in self.edges):
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
        raise NameError(name)

    def __str__(self):
        result = ''

        for source in self.edges:
            for destiny in self.edges[source]:
                result = result + source.getName() + ' -> '\
                    + destiny.getName() + '\n'
        
        # Omit final newline
        return result[:-1]

class Graph(Diagraph):
    def addEdge(self, edge):
        Diagraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())

        Diagraph.addEdge(self, rev)

def buildEuropeRailGraph(graphType):
    g = Graph()

    for name in ('London', 'Paris', 'Brussels', 'Amsterdam',
                 'Berlin', 'Munich', 'Vienna', 'Zurich',
                 'Milan', 'Madrid', 'Barcelona', 'Rome', 'Budapest', 
                 'Hamburg', 'Copenhagen', 'Stockholm'):
        g.addNode(Node(name))

    # Add railway connections (simplified network)
    g.addEdge(Edge(g.getNode('London'), g.getNode('Paris')))
    g.addEdge(Edge(g.getNode('Paris'), g.getNode('Brussels')))
    g.addEdge(Edge(g.getNode('Paris'), g.getNode('Zurich')))
    g.addEdge(Edge(g.getNode('Paris'), g.getNode('Madrid')))
    g.addEdge(Edge(g.getNode('Brussels'), g.getNode('Amsterdam')))
    g.addEdge(Edge(g.getNode('Amsterdam'), g.getNode('Berlin')))
    g.addEdge(Edge(g.getNode('Berlin'), g.getNode('Hamburg')))
    g.addEdge(Edge(g.getNode('Berlin'), g.getNode('Munich')))
    g.addEdge(Edge(g.getNode('Hamburg'), g.getNode('Copenhagen')))
    g.addEdge(Edge(g.getNode('Munich'), g.getNode('Vienna')))
    g.addEdge(Edge(g.getNode('Vienna'), g.getNode('Zurich')))
    g.addEdge(Edge(g.getNode('Vienna'), g.getNode('Budapest')))
    g.addEdge(Edge(g.getNode('Zurich'), g.getNode('Milan')))
    g.addEdge(Edge(g.getNode('Milan'), g.getNode('Rome')))
    g.addEdge(Edge(g.getNode('Milan'), g.getNode('Barcelona')))
    g.addEdge(Edge(g.getNode('Madrid'), g.getNode('Barcelona')))
    g.addEdge(Edge(g.getNode('Copenhagen'), g.getNode('Stockholm')))

    return g


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''

    for i in range(len(path)):
        result = result + str(path[i])

        if i != len(path) - 1:
            result = result + ' -> '

    return result 

# Depth First Search - DFS

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

def testShortestPathDFS(source, destination):
    g = buildEuropeRailGraph(Diagraph)

    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print(f'Shortest path from {source} to {destination} is {printPath(sp)}.\n')

    else:
        print(f"There's no path from {source} to {destination}!\n")

# Breadth First Search - BFS
printQueue = True

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


def testShortestPathBFS(source, destination):
    g = buildEuropeRailGraph(Diagraph)

    sp = shortestPathBFS(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print(f'Shortest path from {source} to {destination} is {printPath(sp)}.\n')

    else:
        print(f"There's no path from {source} to {destination}!\n")


if __name__ == '__main__':
    # What is the shortest path between Paris and Berlin?
    print("Testing the shortest path from Paris to Berlin...")
    testShortestPathBFS('Paris', 'Berlin')

    # What is the shortest path between London and Paris?
    print("Testing the shortest path from London to Paris...")
    testShortestPathBFS('Paris', 'London')

    # What is the shortest path between Budapest and London?
    print("Testing the shortest path from Budapest to London")
    testShortestPathBFS('Budapest', 'Paris')

    # What is the shortest path between Budapest and Stockholm?
    print("Testing the shortest path from Budapest to London")
    testShortestPathBFS('Budapest', 'Stockholm')