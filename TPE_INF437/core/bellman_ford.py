"""
Implémentation académique de l'algorithme de Bellman-Ford
Références:
- Bellman, R. (1958). "On a routing problem"
- Ford, L.R. (1956). "Network flow theory"
- CLRS Chapter 24.1: The Bellman-Ford algorithm
"""

from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass
import sys

@dataclass
class BellmanFordResult:
    """Résultats de Bellman-Ford avec détection de cycles négatifs"""
    distances: List[float]
    predecessors: List[Optional[int]]
    has_negative_cycle: bool
    negative_cycle: List[int] = None
    
    def get_path(self, target: int) -> Optional[List[int]]:
        """Reconstruit le chemin si pas de cycle négatif atteignable"""
        if self.has_negative_cycle:
            return None
        if self.distances[target] == float('inf'):
            return []
        
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = self.predecessors[current]
        return path[::-1]

class BellmanFord:
    """
    Implémentation rigoureuse de Bellman-Ford
    
    Théorème (CLRS Corollary 24.3):
    Soit G = (V,E) avec source s et fonction de poids w: E → ℝ
    Si G ne contient pas de cycle négatif accessible depuis s,
    alors après |V|-1 itérations, d[v] = δ(s,v) pour tout v ∈ V
    
    Complexité: O(VE) - CLRS Lemma 24.2
    """
    
    @staticmethod
    def classic(graph: Graph, source: int) -> BellmanFordResult:
        """
        Version classique avec détection de cycles négatifs
        
        Args:
            graph: graphe orienté pondéré (peut avoir poids négatifs)
            source: sommet source
        
        Returns:
            BellmanFordResult avec distances et indication de cycle négatif
        
        Preuve de correction (CLRS Theorem 24.4):
        Par récurrence sur le nombre d'arêtes dans les plus courts chemins
        """
        n = graph.n
        distances = [float('inf')] * n
        predecessors = [None] * n
        
        # Initialisation (CLRS ligne 1-4)
        distances[source] = 0
        
        # Liste de toutes les arêtes
        edges = graph.edges
        
        # Relâchement |V|-1 fois (CLRS ligne 5-7)
        for i in range(n - 1):
            updated = False
            for edge in edges:
                u, v, weight = edge.source, edge.destination, edge.weight
                
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
                    updated = True
            
            # Optimisation: arrêt précoce si pas de mise à jour
            if not updated:
                break
        
        # Détection de cycles négatifs (CLRS ligne 8-12)
        negative_cycle = None
        has_negative_cycle = False
        
        for edge in edges:
            u, v, weight = edge.source, edge.destination, edge.weight
            if distances[u] + weight < distances[v]:
                has_negative_cycle = True
                negative_cycle = BellmanFord._find_negative_cycle(
                    graph, predecessors, v
                )
                break
        
        return BellmanFordResult(
            distances, 
            predecessors, 
            has_negative_cycle, 
            negative_cycle
        )
    
    @staticmethod
    def _find_negative_cycle(graph: Graph, predecessors: List[Optional[int]], 
                           start: int) -> List[int]:
        """
        Trouve un cycle négatif en utilisant l'algorithme du lièvre et de la tortue
        (Floyd's cycle detection algorithm adapté)
        """
        # Algorithme de détection de cycle
        tortoise = start
        hare = start
        
        while True:
            if predecessors[tortoise] is None or predecessors[predecessors[hare]] is None:
                return []
            
            tortoise = predecessors[tortoise]
            hare = predecessors[predecessors[hare]]
            
            if tortoise == hare:
                break
        
        # Trouver le début du cycle
        tortoise = start
        while tortoise != hare:
            tortoise = predecessors[tortoise]
            hare = predecessors[hare]
        
        # Reconstruire le cycle
        cycle = []
        current = tortoise
        while True:
            cycle.append(current)
            current = predecessors[current]
            if current == tortoise and len(cycle) > 1:
                break
        
        return cycle[::-1]
    
    @staticmethod
    def spfa(graph: Graph, source: int) -> BellmanFordResult:
        """
        SPFA (Shortest Path Faster Algorithm) - optimisation de Bellman-Ford
        Référence: Fanding Duan, 1994
        Meilleur en pratique sur graphes clairsemés
        """
        from collections import deque
        
        n = graph.n
        distances = [float('inf')] * n
        predecessors = [None] * n
        in_queue = [False] * n
        count = [0] * n  # Compteur pour détection de cycle
        
        distances[source] = 0
        queue = deque([source])
        in_queue[source] = True
        
        while queue:
            u = queue.popleft()
            in_queue[u] = False
            
            for edge in graph.adjacency_list[u]:
                v = edge.destination
                new_dist = distances[u] + edge.weight
                
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True
                        count[v] += 1
                        
                        # Détection de cycle négatif
                        if count[v] >= n:
                            cycle = BellmanFord._find_negative_cycle(
                                graph, predecessors, v
                            )
                            return BellmanFordResult(
                                distances, predecessors, True, cycle
                            )
        
        return BellmanFordResult(distances, predecessors, False)