from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        '''
        Karinaville---2040 mi---No--------1520 mi----Fallland
        |                     /    \                  /
        980 mi        1740 mi        1140 mi      1890 mi
        |           /                      \      /
        Sandwichton--------1890 mi--------Martford
        '''
        # defines the graph
        self.g = Graph()
        self.g.add_edge("Karinaville", "No", 2040)
        self.g.add_edge("Karinaville", "Sandwichton", 980)
        self.g.add_edge("No", "Fallland", 1520)
        self.g.add_edge("No", "Martford", 1140)
        self.g.add_edge("Fallland", "Martford", 1890)
        self.g.add_edge("Sandwichton", "Martford", 1890)
        self.g.add_edge("Sandwichton", "No", 1740)
        return self.g
    

    def test_add_edge(self):
        """ checks that all edges were added correctly """
        graph = self.setUp()

        # tests that these cities are connected
        self.assertTrue(graph.has_edge("Karinaville", "No"))
        self.assertTrue(graph.has_edge("Karinaville", "Sandwichton"))
        self.assertTrue(graph.has_edge("No", "Sandwichton"))
        self.assertTrue(graph.has_edge("No", "Fallland"))
        self.assertTrue(graph.has_edge("No", "Martford"))
        self.assertTrue(graph.has_edge("Fallland", "Martford"))

        # tests that these cities are not connected
        self.assertFalse(graph.has_edge("Karinaville", "Fallland"))
        self.assertFalse(graph.has_edge("Fallland", "Karinaville"))


    def test_remove_edge(self):
        """ removes an edge and check that it was removed but nothing else was removed """
        graph = self.setUp()

        # Karinaville and No are no longer connected so they should not be connected
        graph.remove_edge("Karinaville", "No", 2040)
        self.assertFalse(graph.has_edge("Karinaville", "No"))

        # the rest of cities should not be impacted
        self.assertTrue(graph.has_edge("Karinaville", "Sandwichton"))
        self.assertTrue(graph.has_edge("No", "Fallland"))
        self.assertTrue(graph.has_edge("No", "Martford"))
        self.assertTrue(graph.has_edge("Fallland", "Martford"))

    
    def test_nbrs(self):
        """ tests that nbrs returns the neighbors """
        graph = self.setUp()

        # checks that neighbors of No were returned
        neighbors = graph.nbrs("No")
        self.assertTrue("Karinaville" in neighbors)
        self.assertTrue("Fallland" in neighbors)

        # checks that the neighbors of Martford were returned
        neighbors = graph.nbrs("Martford")
        self.assertTrue("Fallland" in neighbors)
        self.assertTrue("Sandwichton" in neighbors)
        
    
class test_GraphTraversal(unittest.TestCase):
    ''' creates a graph `self.g` that you can use in your other unittests '''
    def setUp(self):
        '''
        Karinaville---2040 mi---No--------1520 mi----Fallland
        |                     /    \                  /
        980 mi       1740 mi         1140 mi      1890 mi
        |           /                      \      /
        Sandwichton--------1890 mi--------Martford
        '''
        # defines the graph
        self.g = Graph()
        self.g.add_edge("Karinaville", "No", 2040)
        self.g.add_edge("Sandwichton", "No", 1740)
        self.g.add_edge("Karinaville", "Sandwichton", 980)
        self.g.add_edge("No", "Fallland", 1520)
        self.g.add_edge("No", "Martford", 1140)
        self.g.add_edge("Fallland", "Martford", 1890)
        self.g.add_edge("Sandwichton", "Martford", 1890)
        return self.g


    # Alg: breadth first search
    # Why: this algorithm calculates the route to other cities with the amount of stops in other vertexes
    def test_fewest_flights(self):
        ''' tests how many "flights" are needed to be taken from Karinaville to each city '''
        graph = self.setUp()
        '''
        Karinaville to Karinaville: 0 (lol)
        Karinaville to No: 1
        Karinaville to Sandwichton: 1
        Karinaville to Martford: 2
        Karinaville to Fallland: 2
        '''
        x, flights = graph.fewest_flights("Karinaville")
        expected_flights = {"Karinaville": 0, "No": 1, "Fallland": 2, "Sandwichton": 1, "Martford": 2}
        self.assertDictEqual(flights, expected_flights)
 

    # Alg: Dijkstra's algorithm
    # Why: this specific algorithm finds the shortest path from a city to every other city taking weight into account
    def test_shortest_path(self):
        ''' finds the shortest distance from Karinaville to every city '''
        graph = self.setUp()
        x, distances = graph.shortest_path("Karinaville")
        '''
        Karinaville to Karinaville: 0 (lol)
        Karinaville to No: 2040
        Karinaville to Sandwichton: 980
        Karinaville to Martford: 980 + 1890 = 2870
        Karinaville to Fallland: 2040 + 1520 = 3560
        '''
        expected_distances = {"Karinaville": 0, "No": 2040, "Sandwichton": 980, "Martford": 2870, "Fallland": 3560,}
        self.assertDictEqual(distances, expected_distances)


    # Alg: Prim's algorithm
    # Why: this algorithm connects all the vertexes with minimum sized edges
    def test_minimum_salt(self):
        '''
        original route:
                                Karinaville---2040 mi---No--------1520 mi----Fallland
                                |                     /    \                  /
                                980 mi       1740 mi         1140 mi      1890 mi
                                |           /                      \      /
                                Sandwichton--------1890 mi--------Martford
        total miles: 9460

        minimum miles route:
                                Karinaville---2040 mi------No---1520 mi----Fallland
                                |                           \                   
                                980 mi                       1140 mi
                                |                                 \             
                                Sandwichton                       Martford
        total miles: 5680
        '''
        # tests that the minimum_salt algorithm adds up the minimum miles to connect each city
        graph = self.setUp()
        x, vertex_weights = graph.minimum_salt("Karinaville")
        expected_weights = 5680
        self.assertEqual(sum(vertex_weights.values()), expected_weights)


unittest.main()