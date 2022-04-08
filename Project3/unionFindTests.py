'''
Union-Find data structure tests
Based on DPV Section 5.1.4, specifically figures 5.6 and 5.7
'''
from mst import unionFind
import unittest

class UnionFindTests(unittest.TestCase):
    def testCreation(self):
        uf = unionFind(7)
        self.assertEqual(uf.pi, list(range(7)))
        self.assertEqual(uf.rank, [0] * 7)

    def testFind(self):
        uf = unionFind(11)
        #          0  1  2  3  4  5  6  7  8  9  10
        #          A  B  C  D  E  F  G  H  I  J  K
        uf.pi =   [0, 0, 0, 2, 0, 4, 4, 4, 5, 5, 6]
        uf.rank = [3, 0, 1, 0, 2, 1, 1, 0, 0, 0, 0]

        # find I
        uf.find(8)
        #                          0  1  2  3  4  5  6  7  8  9  10
        #                          A  B  C  D  E  F  G  H  I  J  K
        self.assertEqual(uf.pi,   [0, 0, 0, 2, 0, 0, 4, 4, 0, 5, 6])
        self.assertEqual(uf.rank, [3, 0, 1, 0, 2, 1, 1, 0, 0, 0, 0])

        # find K
        uf.find(10)
        #                          0  1  2  3  4  5  6  7  8  9  10
        #                          A  B  C  D  E  F  G  H  I  J  K
        self.assertEqual(uf.pi,   [0, 0, 0, 2, 0, 0, 0, 4, 0, 5, 0])
        self.assertEqual(uf.rank, [3, 0, 1, 0, 2, 1, 1, 0, 0, 0, 0])

    def testUnions(self):
        # Create A, ..., G
        uf = unionFind(7)

        # union(A,D), union(B,E), union(C,F)
        uf.union(0, 3)
        uf.union(1, 4)
        uf.union(2, 5)
        self.assertEqual(uf.pi, [3, 4, 5, 3, 4, 5, 6])
        self.assertEqual(uf.rank, [0, 0, 0, 1, 1, 1, 0])

        # union(C,G), union(E,A)
        uf.union(2, 6)
        uf.union(4, 0)
        self.assertEqual(uf.pi, [3, 4, 5, 3, 3, 5, 5])
        self.assertEqual(uf.rank, [0, 0, 0, 2, 1, 1, 0])

        # union(B, G)
        uf.union(1, 6)
        self.assertEqual(uf.pi, [3, 3, 5, 3, 3, 3, 5])
        self.assertEqual(uf.rank, [0, 0, 0, 2, 1, 1, 0])

if __name__ == '__main__':
    unittest.main()