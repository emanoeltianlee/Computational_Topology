from src.BoundaryOperator import BoundaryOperator
from collections import Counter

class Homology:
    @staticmethod
    def compute_homology(chain_complex):
        homology_groups = {}
        for dim, simplices in chain_complex.chain_groups.items():
            boundaries = Counter()
            for simplex in simplices:
                for boundary in BoundaryOperator.boundary(simplex):
                    boundaries[boundary] += 1
            kernel = [s for s, count in boundaries.items() if count % 2 == 0]
            image = [s for s, count in boundaries.items() if count % 2 != 0]
            homology_groups[dim] = len(kernel) - len(image)
        return homology_groups