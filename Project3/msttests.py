import GA_ProjectUtils as utils
import mst

import unittest
import itertools
from collections import Counter

class MstTest(unittest.TestCase):
    """
    Unit tests for CS6515, Coding Project 3: Kruskal, Spring 2022.

    Author: Tim West (timwest@gatech.edu)

    This resource is unofficial and not guaranteed to be
    comprehensive or correct. Please use at your own risk.

    Last Updated: 4/5/2022 01:45 ET
    """
    def verifyRootPointers(self, uf):
        """Helper to verify MST is fully connected."""
        num_vertices = len(uf.rank)
        for u, v in itertools.permutations(range(num_vertices), 2):
            self.assertTrue(uf.areConnected(u, v))

    def verifyUnionFindProps(self, uf):
        self.verifyProp1(uf)
        self.verifyProp3(uf)

    def verifyProp1(self, uf):
        """Verifies Property 1 of Union-Find."""
        for x in range(len(uf.rank)):
            uf.rank[x] < uf.rank[uf.pi[x]]

    def verifyProp3(self, uf):
        """Verifies Property 3 of Union-Find."""
        n = len(uf.rank)
        count_dict = Counter(uf.rank)
        for k, count in count_dict.items():
            count <= n/2**k

    def test_simple(self):
        """Tests with 2 vertices & 1 edge."""
        G = utils.Graph(2, [[1, 0, 1]])
        MST, uf = mst.kruskal(G)
        self.assertEqual(len(MST), 1)
        self.assertEqual(utils.findTotalWeightOfMst(MST), 1)
        self.assertTrue(uf.areConnected(0, 1))

    def test_cycle_lower(self):
        """Tests that the heaviest edge is not taken in the cycle."""
        G = utils.Graph(3, [[1, 0, 1], [1, 1, 2], [2, 2, 0]])
        MST, uf = mst.kruskal(G)
        self.assertEqual(len(MST), 2)
        self.assertEqual(utils.findTotalWeightOfMst(MST), 2)
        self.verifyRootPointers(uf)
        self.verifyUnionFindProps(uf)

    def test_take_heaviest(self):
        """Tests that the heaviest edge must be taken."""
        G = utils.Graph(4, [[1, 0, 1], [1, 1, 2], [3, 2, 3]])
        MST, uf = mst.kruskal(G)
        self.assertEqual(len(MST), 3)
        self.assertEqual(utils.findTotalWeightOfMst(MST), 5)
        self.verifyRootPointers(uf)
        self.verifyUnionFindProps(uf)

    def test_take_any(self):
        """Tests any 2 of 3 edges are taken."""
        G = utils.Graph(3, [[1, 0, 1], [1, 1, 2], [1, 2, 0]])
        MST, uf = mst.kruskal(G)
        self.assertEqual(len(MST), 2)
        self.assertEqual(utils.findTotalWeightOfMst(MST), 2)
        self.verifyRootPointers(uf)
        self.verifyUnionFindProps(uf)

    def test_5_1(self):
        """Tests DPV Exercise 5.1."""
        G = utils.Graph(8, [
            [6, 0, 1],
            [5, 1, 2],
            [6, 2, 3],
            [1, 0, 4],
            [2, 1, 4],
            [2, 1, 5],
            [1, 5, 4],
            [5, 2, 5],
            [4, 2, 6],
            [3, 6, 5],
            [5, 3, 6],
            [7, 3, 7],
            [3, 7, 6]
        ])
        MST, uf = mst.kruskal(G)
        self.assertEqual(len(MST), 7)
        self.assertEqual(utils.findTotalWeightOfMst(MST), 19)
        self.verifyRootPointers(uf)
        self.verifyUnionFindProps(uf)

    def test_5_2(self):
        """Tests DPV Exercise 5.2."""
        G = utils.Graph(8, [
            [1, 0, 1],
            [2, 1, 2],
            [3, 2, 3],
            [4, 0, 4],
            [8, 0, 5],
            [5, 4, 5],
            [6, 1, 5],
            [6, 1, 6],
            [1, 5, 6],
            [2, 2, 6],
            [1, 3, 6],
            [1, 7, 6],
            [4, 3, 7]
        ])
        MST, uf = mst.kruskal(G)
        self.assertEqual(len(MST), 7)
        self.assertEqual(utils.findTotalWeightOfMst(MST), 12)
        self.verifyRootPointers(uf)
        self.verifyUnionFindProps(uf)

if __name__ == '__main__':
    unittest.main()