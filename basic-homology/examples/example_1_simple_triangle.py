from SimplicialComplex import SimplicialComplex
from ChainComplex import ChainComplex
from Homology import Homology

vertices = ['A', 'B', 'C']
simplices = [['A', 'B'], ['B', 'C'], ['C', 'A'], ['A', 'B', 'C']]

simplicial_complex = SimplicialComplex(vertices, simplices)
chain_complex = ChainComplex(simplicial_complex)

homology_groups = Homology.compute_homology(chain_complex)

print("Homology groups:", homology_groups)