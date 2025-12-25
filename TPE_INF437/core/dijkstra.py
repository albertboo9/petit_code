"""
Implémentation rigoureuse de l'algorithme de Dijkstra
Références principales:
- Dijkstra, E.W. (1959). "A note on two problems in connexion with graphs"
- CLRS Chapter 24.3: Dijkstra's algorithm
- Fredman & Tarjan (1987). "Fibonacci heaps and their uses"
"""

import sys
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import heapq

@dataclass
class DijkstraResult:
    """Structure pour stocker les résultats de Dijkstra (CLRS p. 658)"""
    distances: List[float]
    predecessors: List[Optional[int]]
    visited_order: List[int]
    
    def get_path(self, target: int) -> List[int]:
        """Reconstruit le chemin de la source à target"""
        if self.distances[target] == float('inf'):
            return []
        
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = self.predecessors[current]
        return path[::-1]

class Dijkstra:
    """
    Implémentation académique de l'algorithme de Dijkstra avec tas binaire
    
    Théorème (CLRS Theorem 24.6):
    Dijkstra(G, w, s) termine avec d[v] = δ(s,v) pour tout v ∈ V
    Preuve par invariant de boucle
    
    Complexité: O((V + E) log V) avec tas binaire
    """
    
    @staticmethod
    def classic(graph: Graph, source: int) -> DijkstraResult:
        """
        Version classique avec file de priorité basée sur tas
        
        Args:
            graph: graphe pondéré non-négatif (condition w(u,v) ≥ 0)
            source: sommet source
        
        Returns:
            DijkstraResult contenant distances et prédécesseurs
        
        Invariant (CLRS p. 659):
        Pour chaque sommet v ∈ S, d[v] = δ(s,v)
        """
        n = graph.n
        distances = [float('inf')] * n
        predecessors = [None] * n
        visited = [False] * n
        visited_order = []
        
        # Initialisation (CLRS ligne 1-5)
        distances[source] = 0
        priority_queue = [(0, source)]  # (distance, vertex)
        
        # Exploration (CLRS ligne 6-16)
        while priority_queue:
            current_dist, u = heapq.heappop(priority_queue)
            
            if visited[u]:
                continue
                
            visited[u] = True
            visited_order.append(u)
            
            # Relâchement des arêtes (CLRS RELAX procedure)
            for edge in graph.adjacency_list[u]:
                v = edge.destination
                new_dist = current_dist + edge.weight
                
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    heapq.heappush(priority_queue, (new_dist, v))
        
        return DijkstraResult(distances, predecessors, visited_order)
    
    @staticmethod
    def with_custom_heap(graph: Graph, source: int) -> DijkstraResult:
        """
        Version utilisant une structure de tas personnalisée
        Illustre l'optimisation possible avec tas de Fibonacci (O(E + V log V))
        """
        from .heap import FibonacciHeap  # Implémentation séparée
        
        n = graph.n
        distances = [float('inf')] * n
        predecessors = [None] * n
        visited_order = []
        
        distances[source] = 0
        heap = FibonacciHeap()
        node_refs = [None] * n
        
        # Initialisation du tas
        for v in range(n):
            if v == source:
                node_refs[v] = heap.insert(0, v)
            else:
                node_refs[v] = heap.insert(float('inf'), v)
        
        # Exploration principale
        while not heap.is_empty():
            u_dist, u = heap.extract_min()
            visited_order.append(u)
            
            for edge in graph.adjacency_list[u]:
                v = edge.destination
                new_dist = u_dist + edge.weight
                
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    heap.decrease_key(node_refs[v], new_dist)
        
        return DijkstraResult(distances, predecessors, visited_order)
    
    @staticmethod
    def analyze_complexity(graph: Graph) -> Dict[str, float]:
        """
        Analyse empirique de la complexité
        Confirme O((V+E)log V) théorique
        """
        import time
        import math
        
        results = {}
        
        for source in [0, graph.n // 2, graph.n - 1]:
            start = time.perf_counter()
            Dijkstra.classic(graph, source)
            end = time.perf_counter()
            
            V = graph.n
            E = sum(len(adj) for adj in graph.adjacency_list.values())
            if not graph.directed:
                E = E // 2
    
            # Ratio complexité empirique / théorique
            empirical_time = end - start
            theoretical_complexity = (V + E) * math.log2(V + 1)
            
            results[f"source_{source}"] = {
                "time": empirical_time,
                "V": V,
                "E": E,
                "ratio": empirical_time / theoretical_complexity * 1e6
            }
        
        return results