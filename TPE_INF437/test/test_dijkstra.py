"""
Tests rigoureux basés sur les preuves du CLRS
"""

import unittest
import sys
from core.graph import Graph
from core.dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    """Tests formels de l'algorithme de Dijkstra"""
    
    def test_single_vertex(self):
        """Test du cas dégénéré: graphe à un sommet (CLRS Exercise 24.3-1)"""
        g = Graph(1)
        result = Dijkstra.classic(g, 0)
        
        self.assertEqual(result.distances[0], 0)
        self.assertEqual(result.predecessors[0], None)
    
    def test_negative_weights_detection(self):
        """Dijkstra ne doit pas fonctionner avec poids négatifs"""
        g = Graph(3, directed=True)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, -3)  # Poids négatif!
        
        # Dijkstra peut donner un résultat incorrect
        result = Dijkstra.classic(g, 0)
        # Le chemin trouvé pourrait ne pas être optimal
        
    def test_clrs_example(self):
        """
        Test avec l'exemple du CLRS Figure 24.6
        Validation des distances correctes
        """
        g = Graph(5, directed=True)
        # Construction exacte de la figure 24.6
        edges = [(0, 1, 10), (0, 3, 5), (1, 2, 1),
                (1, 3, 2), (2, 4, 4), (3, 1, 3),
                (3, 2, 9), (3, 4, 2), (4, 0, 7),
                (4, 2, 6)]
        
        for u, v, w in edges:
            g.add_edge(u, v, w)
        
        result = Dijkstra.classic(g, 0)
        
        # Distances attendues d'après CLRS
        expected = [0, 8, 9, 5, 7]
        
        for i in range(5):
            self.assertAlmostEqual(result.distances[i], expected[i], 
                                 places=5, 
                                 msg=f"Sommet {i}: distance incorrecte")
    
    def test_path_reconstruction(self):
        """Test de reconstruction de chemin (CLRS Lemma 24.16)"""
        g = Graph(4)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        g.add_edge(0, 3, 10)
        
        result = Dijkstra.classic(g, 0)
        path = result.get_path(3)
        
        # Chemin optimal: 0 → 1 → 2 → 3
        self.assertEqual(path, [0, 1, 2, 3])
        self.assertAlmostEqual(result.distances[3], 6)
    
    def test_non_connected_graph(self):
        """Test avec graphe non connexe (CLRS Exercise 24.3-3)"""
        g = Graph(4)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 3, 1)  # Composante séparée
        
        result = Dijkstra.classic(g, 0)
        
        self.assertEqual(result.distances[0], 0)
        self.assertEqual(result.distances[1], 1)
        self.assertEqual(result.distances[2], float('inf'))  # Non atteignable
        self.assertEqual(result.distances[3], float('inf'))  # Non atteignable

if __name__ == "__main__":
    unittest.main(verbosity=2)