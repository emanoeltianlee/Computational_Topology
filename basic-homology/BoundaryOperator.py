from itertools import combinations

class BoundaryOperator:
    @staticmethod
    def boundary(simplex):
        simplex = list(simplex)
        boundary = []
        for i in range(len(simplex)):
            face = frozenset(simplex[:i] + simplex[i+1:])
            boundary.append(((-1) ** i, face))
        return boundary