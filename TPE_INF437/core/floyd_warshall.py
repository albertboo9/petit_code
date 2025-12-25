"""
Implémentation académique de l'algorithme de Floyd-Warshall
Références:
- Floyd, R.W. (1962). "Algorithm 97: Shortest Path"
- Warshall, S. (1962). "A theorem on Boolean matrices"
- CLRS Chapter 25.2: The Floyd-Warshall algorithm
- Kleene's algorithm pour la fermeture transitive
"""

from typing import List, Tuple, Optional
import numpy as np
from dataclasses import dataclass

@dataclass
class FloydWarshallResult:
    """Résultats complets de Floyd-Warshall"""
    distances: List[List[float]]
    predecessors: List[List[Optional[int]]]
    negative_cycles: List[List[int]]
    
    def get_path(self, u: int, v: int) -> Optional[List[int]]:
        """Reconstruit le chemin de u à v si possible"""
        if self.distances[u][v] == float('inf'):
            return None
        
        if self.predecessors[u][v] is None:
            return [] if u == v else None
        
        path = []
        self._reconstruct_path(u, v, path)
        return path
    
    def _reconstruct_path(self, u: int, v: int, path: List[int]) -> None:
        """Helper récursif pour reconstruction de chemin"""
        if self.predecessors[u][v] is None:
            path.append(u)
            if u != v:
                path.append(v)
        else:
            intermediate = self.predecessors[u][v]
            self._reconstruct_path(u, intermediate, path)
            path.pop()  # Enlever le doublon
            self._reconstruct_path(intermediate, v, path)

class FloydWarshall:
    """
    Implémentation rigoureuse de Floyd-Warshall
    
    Théorème (CLRS Theorem 25.1):
    Après exécution de Floyd-Warshall, D[i][j] = δ(i,j) pour tout i,j ∈ V
    à moins qu'il existe un cycle négatif sur un chemin de i à j
    
    Complexité: Θ(V³) - CLRS p. 694
    """
    
    @staticmethod
    def classic(graph: Graph) -> FloydWarshallResult:
        """
        Version classique avec reconstruction de chemins
        
        Args:
            graph: graphe orienté pondéré
        
        Returns:
            FloydWarshallResult avec toutes paires de distances
        
        Preuve par programmation dynamique (CLRS p. 692):
        d_ij^(k) = poids min d'un chemin de i à j utilisant seulement {1,...,k}
        Relation de récurrence: d_ij^(k) = min(d_ij^(k-1), d_ik^(k-1) + d_kj^(k-1))
        """
        n = graph.n
        INF = float('inf')
        
        # Initialisation (CLRS ligne 1-4)
        distances = [[INF] * n for _ in range(n)]
        predecessors = [[None] * n for _ in range(n)]
        
        for i in range(n):
            distances[i][i] = 0
            for edge in graph.adjacency_list[i]:
                j = edge.destination
                distances[i][j] = edge.weight
                predecessors[i][j] = i
        
        # Programmation dynamique (CLRS ligne 5-11)
        for k in range(n):
            for i in range(n):
                if distances[i][k] == INF:
                    continue
                for j in range(n):
                    new_dist = distances[i][k] + distances[k][j]
                    if new_dist < distances[i][j]:
                        distances[i][j] = new_dist
                        predecessors[i][j] = predecessors[k][j]
        
        # Détection de cycles négatifs
        negative_cycles = FloydWarshall._detect_negative_cycles(distances)
        
        return FloydWarshallResult(distances, predecessors, negative_cycles)
    
    @staticmethod
    def _detect_negative_cycles(distances: List[List[float]]) -> List[List[int]]:
        """
        Détecte les cycles négatifs dans la matrice des distances
        Un cycle négatif existe si D[i][i] < 0 pour un i
        
        Théorème (CLRS p. 697): D[i][i] < 0 ssi il existe un cycle négatif contenant i
        """
        n = len(distances)
        cycles = []
        
        for i in range(n):
            if distances[i][i] < 0:
                # Cycle négatif détecté - reconstruction simplifiée
                cycle = [i]
                current = i
                for _ in range(n):  # Par sécurité
                    # Chercher un prédécesseur menant à un chemin négatif
                    for j in range(n):
                        if j != current and distances[j][current] + distances[current][j] < 0:
                            cycle.append(j)
                            current = j
                            break
                    if cycle[-1] == i and len(cycle) > 1:
                        break
                cycles.append(cycle)
        
        return cycles
    
    @staticmethod
    def transitive_closure(graph: Graph) -> List[List[bool]]:
        """
        Calcule la fermeture transitive d'un graphe
        Algorithme de Warshall (1962)
        
        Complexité: O(V³) mais plus simple que Floyd-Warshall
        """
        n = graph.n
        reachable = [[False] * n for _ in range(n)]
        
        for i in range(n):
            reachable[i][i] = True
            for edge in graph.adjacency_list[i]:
                reachable[i][edge.destination] = True
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        
        return reachable
    
    @staticmethod
    def optimized_with_numpy(graph: Graph) -> np.ndarray:
        """
        Version optimisée utilisant NumPy pour les opérations matricielles
        Illustre l'optimisation par bloc et vectorisation
        """
        import numpy as np
        
        n = graph.n
        INF = float('inf')
        
        # Initialisation avec NumPy
        D = np.full((n, n), INF)
        np.fill_diagonal(D, 0)
        
        for i in range(n):
            for edge in graph.adjacency_list[i]:
                D[i, edge.destination] = edge.weight
        
        # Algorithme de Floyd-Warshall vectorisé
        for k in range(n):
            # Opération vectorisée: D[i,j] = min(D[i,j], D[i,k] + D[k,j])
            through_k = D[:, k:k+1] + D[k:k+1, :]
            D = np.minimum(D, through_k)
        
        return D