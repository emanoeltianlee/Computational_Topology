from collections import defaultdict

class ChainComplex:
    def __init__(self, simplicial_complex):
        self.simplicial_complex = simplicial_complex
        self.chain_groups = self.build_chain_groups()

    def build_chain_groups(self):
        chain_groups = defaultdict(list)
        for simplex in self.simplicial_complex.simplices:
            chain_groups[len(simplex) - 1].append(simplex)
        return chain_groups