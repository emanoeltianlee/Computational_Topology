from src.SimplicialComplex import SimplicialComplex
from src.ChainComplex import ChainComplex
from src.Homology import Homology

vertices = ['A', 'B', 'C', 'D']
simplices = [
    ['A', 'B'], ['A', 'C'], ['A', 'D'],
    ['B', 'C'], ['B', 'D'], ['C', 'D'],
    ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'],
    ['A', 'B', 'C', 'D']
]

simplicial_complex = SimplicialComplex(vertices, simplices)
chain_complex = ChainComplex(simplicial_complex)
homology_groups = Homology.compute_homology(chain_complex)

print("Homology groups:", homology_groups)