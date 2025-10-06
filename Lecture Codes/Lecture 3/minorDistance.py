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
    
# Weighted Edge
class weightedEdge(Edge):
    """ Assumes source and destiny are Nodes, weight is a number """
    def __init__(self, source, destiny, weight = 1.0):
        self.source = source
        self.destiny = destiny
        self.weight = weight
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return self.source.getName() + ' -> (' + str(self.weight) + ')'\
                + self.destiny.getName()
    
class Digraph(object):
    """ Edges is a dictionary mapping each node to a list of its children """
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        """ Nodes are represented as keys in dictionary """
        if node in self.edges:
            raise ValueError('Duplicated Node')
        else:
            self.edges[node] = []
    
    def addEdge(self, edge, weight):
        """ Edges are represented by destinations as values in list associated with a source key"""
        source = edge.getSource()
        destiny = edge.getDestination()
        weight = edge.getWeight()
        
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

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())

        Digraph.addEdge(self, rev)

# Cities
def buildCityGraph():
    g = Graph()

    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): # Creates 7 cities nodes
        g.addNode(Node(name))

    # Associates each node to edges    
    g.addEdge(weightedEdge(g.getNode('Boston'), g.getNode('Providence'), 80))
    g.addEdge(weightedEdge(g.getNode('Boston'), g.getNode('New York'), 349))
    g.addEdge(weightedEdge(g.getNode('Providence'), g.getNode('Boston'), 80))
    g.addEdge(weightedEdge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(weightedEdge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(weightedEdge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(weightedEdge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(weightedEdge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(weightedEdge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(weightedEdge(g.getNode('Los Angeles'), g.getNode('Boston')))

    return g

if __name__ == '__main__':
    cities = buildCityGraph()

    print(f'{cities}')