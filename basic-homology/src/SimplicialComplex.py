from itertools import combinations

class SimplicialComplex:
    def __init__(self, vertices, simplices):
        self.vertices = set(vertices)
        self.simplices = set(frozenset(simplex) for simplex in simplices)
        self.update_complex()

    def update_complex(self):
        for simplex in list(self.simplices):
            for k in range(1, len(simplex)):
                for face in combinations(simplex, k):
                    self.simplices.add(frozenset(face))

    def add_simplex(self, simplex):
        self.simplices.add(frozenset(simplex))
        self.update_complex()