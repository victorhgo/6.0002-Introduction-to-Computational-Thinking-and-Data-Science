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
        raise NameError(name)

    def __str__(self):
        result = ''

        for source in self.edges:
            for destiny in self.edges[source]:
                result = result + source.getName() + '->'\
                    + destiny.getName() + '\n'
        
        # Omit final newline
        return result[:-1]

class Graph(Diagraph):
    def addEdge(self, edge):
        Diagraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())

        Diagraph.addEdge(self, rev)

if __name__ == '__main__':
    pass

