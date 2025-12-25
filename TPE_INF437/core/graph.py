"""
Module de structures de graphes inspiré de:
- CLRS Chapter 22: Elementary Graph Algorithms
- Knuth, TAOCP Vol. 1: Fundamental Algorithms
"""

from typing import Dict, List, Tuple, Optional, Union
import heapq
from dataclasses import dataclass
from enum import Enum

class GraphType(Enum):
    """Types de graphes selon les classifications académiques"""
    DIRECTED = "directed"
    UNDIRECTED = "undirected"
    WEIGHTED = "weighted"
    UNWEIGHTED = "unweighted"

@dataclass
class Edge:
    """Représentation d'une arête avec métadonnées"""
    source: int
    destination: int
    weight: float
    label: Optional[str] = None
    
    def __repr__(self) -> str:
        return f"({self.source} → {self.destination} : {self.weight})"

class Graph:
    """
    Implémentation professionnelle d'un graphe selon CLRS Section 22.1
    Supporte plusieurs représentations: liste d'adjacence et matrice d'adjacence
    """
    
    def __init__(self, vertices: int, directed: bool = False):
        """
        Initialise un graphe avec n sommets
        
        Args:
            vertices: nombre de sommets
            directed: True pour un graphe orienté (CLRS Def. B.4)
        """
        self.n = vertices
        self.directed = directed
        self.adjacency_list: Dict[int, List[Edge]] = {i: [] for i in range(vertices)}
        self.vertices_data: Dict[int, Dict] = {}  # Pour les algorithmes avancés
        
    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        """
        Ajoute une arête u → v avec poids weight
        Complexité: O(1) amorti (CLRS Lemma 22.1)
        """
        edge = Edge(u, v, weight)
        self.adjacency_list[u].append(edge)
        
        if not self.directed:
            reverse_edge = Edge(v, u, weight)
            self.adjacency_list[v].append(reverse_edge)
    
    def get_neighbors(self, vertex: int) -> List[Tuple[int, float]]:
        """Retourne les voisins d'un sommet avec leurs poids"""
        return [(edge.destination, edge.weight) for edge in self.adjacency_list[vertex]]
    
    def get_weight(self, u: int, v: int) -> Optional[float]:
        """
        Retourne le poids de l'arête (u,v) ou None si elle n'existe pas
        Implémentation optimisée selon Knuth's TAOCP Vol. 1, Section 2.3
        """
        for edge in self.adjacency_list[u]:
            if edge.destination == v:
                return edge.weight
        return None
    
    @property
    def edges(self) -> List[Edge]:
        """Retourne toutes les arêtes du graphe (CLRS Def. B.4)"""
        edges = []
        for vertex in range(self.n):
            for edge in self.adjacency_list[vertex]:
                if self.directed or edge.destination >= vertex:
                    edges.append(edge)
        return edges
    
    def to_adjacency_matrix(self) -> List[List[float]]:
        """
        Convertit en matrice d'adjacence
        Complexité: O(V²) - Théorème CLRS 22.1
        """
        INF = float('inf')
        matrix = [[INF] * self.n for _ in range(self.n)]
        
        for i in range(self.n):
            matrix[i][i] = 0  # diagonale à zéro
            for edge in self.adjacency_list[i]:
                matrix[i][edge.destination] = edge.weight
        
        return matrix