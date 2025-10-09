# 6.0002 Problem Set 2
# Graph optimization
# Name: Victor Correa
# Time: 4h30m

# =============================================
# Finding shortest paths through MIT buildings
# =============================================

import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer: The nodes represent buildings, the edges represent the distance
# between two buildings and also the distance outdoor. The distances are represented
# in the WeightedEdge

# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    print(f"Loading map from file {map_filename}...")

    # Create a Digraph g object
    g = Digraph()

    with open(map_filename, 'r') as file:

        # Iterate over each file's line
        for line in file:
            if line.strip() == '':
                continue
        
            # Split line into the following components: source building, dest building, total distance, outdoor distance
            src_building, dest_building, total_dist, outdoor_dist = line.split()

            src = Node(src_building)
            dest = Node(dest_building)

            # Add the nodes to the Diagraph
            if not g.has_node(src):
                g.add_node(src)
            if not g.has_node(dest):
                g.add_node(dest)

            # Create the weighted edges
            edge = WeightedEdge(src, dest, int(total_dist), int(outdoor_dist))
            g.add_edge(edge)

    return g

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out
#    g = load_map("test_load_map.txt")
#    print(g)


# Problem 3: Finding the Shortest Path using Optimized Search Method

# Problem 3a: Objective function

# What is the objective function for this problem? What are the constraints?

# Answer: The objective of this function is to find the best path between buildings, avoiding
# spending too much time outdoors (the constraints for this problem)

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    if not (digraph.has_node(start) and digraph.has_node(end)):
        raise ValueError('Node not in graph')
    
    # To avoid mutation on the recursive calls
    path = [path[0] + [start], path[1], path[2]]

    # Base case: reached the destination
    if start == end:
        return path
    
    # Check all outgoing edges
    for edge in digraph.get_edges_for_node(start):
        dest = edge.get_destination()

        # To avoid cycles
        if dest in path[0]:
            continue

        # Distances: total and outdoor
        total_dist = path[1] + edge.get_total_distance()
        outdoor_dist = path[2] + edge.get_outdoor_distance()

        # Constraints for travel
        if outdoor_dist > max_dist_outdoors:
            continue
        if best_dist is not None and total_dist >= best_dist:
            continue
    
        # Recursive call
        new_path = get_best_path(digraph, dest, end, [path[0], 
                                total_dist, outdoor_dist], max_dist_outdoors, 
                                best_dist, best_path)

        # If we have found a valid path, update the best one
        if new_path is not None:
            new_total_dist = new_path[1]

            if best_dist is None or new_total_dist < best_dist:
                best_path = new_path[0]
                best_dist = new_total_dist

    if best_path is None:
        return None
    else:
        return [best_path, best_dist, None]


# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    startNode = Node(start)
    endNode = Node(end)

    if not (digraph.has_node(startNode) and digraph.has_node(endNode)):
        raise ValueError("Node not found in Graph!")
    
    # Get best path
    best_path = get_best_path(digraph, startNode, endNode,
                              [[], 0, 0], max_dist_outdoors,
                              None, None)
    
    # No valid path could be found
    if best_path is None:
        raise ValueError("A valid path could not be found.")
    
    total_dist = best_path[1]

    if total_dist > max_total_dist:
        raise ValueError("No path can be found to satisfy constraints!")

    return best_path[0]
    
# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
