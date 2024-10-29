import unittest
from SimplicialComplex import SimplicialComplex

class TestSimplicialComplex(unittest.TestCase):
    def test_add_simplex(self):
        vertices = ['A', 'B', 'C']
        simplices = [['A', 'B'], ['B', 'C']]
        complex = SimplicialComplex(vertices, simplices)

        self.assertIn(frozenset(['A', 'B']), complex.simplices)
        self.assertIn(frozenset(['B', 'C']), complex.simplices)

        complex.add_simplex(['A', 'C'])
        self.assertIn(frozenset(['A', 'C']), complex.simplices)


if __name__ == '__main__':
    unittest.main()