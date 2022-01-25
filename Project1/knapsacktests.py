import unittest
from knapsack import knapsack


class TestKnapsack(unittest.TestCase):
    '''
    Unit tests for CS6515, Coding Project 1: Knapsack.

    Author: Tim West (timwest@gatech.edu)

    This resource is unofficial and not guaranteed to be
    comprehensive or correct. Please use at your own risk.

    Last Updated: 1/24/2022, 11:03 PM ET
    '''

    def test_none(self):
        '''According to assignment docstring, this is not a required case.'''
        self.assertEqual(knapsack({1: ('x', 2, 1)}, 1), [])

    def test_simple(self):
        self.assertEqual(knapsack({1: ('x', 1, 1)}, 1), [('x', 1, 1)])

    def test_all(self):
        ans = sorted(knapsack({1: ('x', 1, 1), 2: ('y', 3, 1)}, 4))
        self.assertEqual(ans, [('x', 1, 1), ('y', 3, 1)])

    def test_take_fit(self):
        ans = knapsack({1: ('x', 20, 1), 2: ('y', 30, 1)}, 25)
        self.assertEqual(ans, [('x', 20, 1)])

    def test_take_max(self):
        ans = knapsack({1: ('x', 5, 10), 2: ('y', 1, 20)}, 5)
        self.assertEqual(ans, [('y', 1, 20)])

    def test_not_greedy(self):
        ans = sorted(knapsack({1: ('x', 1, 10), 2: ('y', 5, 20), 3: ('z', 4, 15)}, 5))
        self.assertEqual(ans, [('x', 1, 10), ('z', 4, 15)])

    def test_any_one(self):
        ans = knapsack({1: ('x', 5, 10), 2: ('y', 5, 10)}, 5)
        self.assertIn(ans, [[('x', 5, 10)], [('y', 5, 10)]])
        self.assertNotEqual(ans, [('x', 5, 10), ('y', 5, 10)])

    def test_increasing_all(self):
        ans = sorted(knapsack({1: ('w', 1, 1), 2: ('x', 2, 2), 3: ('y', 3, 3), 4: ('z', 4, 4)}, 10))
        self.assertEqual(ans, [('w', 1, 1), ('x', 2, 2), ('y', 3, 3), ('z', 4, 4)])

    def test_increasing(self):
        ans = sorted(knapsack({1: ('w', 1, 1), 2: ('x', 2, 2), 3: ('y', 3, 3), 4: ('z', 4, 4)}, 9))
        self.assertEqual(ans, [('x', 2, 2), ('y', 3, 3), ('z', 4, 4)])

    def test_decreasing_all(self):
        ans = sorted(knapsack({1: ('w', 4, 4), 2: ('x', 3, 3), 3: ('y', 2, 2), 4: ('z', 1, 1)}, 10))
        self.assertEqual(ans, [('w', 4, 4), ('x', 3, 3), ('y', 2, 2), ('z', 1, 1)])

    def test_decreasing(self):
        ans = sorted(knapsack({1: ('w', 4, 4), 2: ('x', 3, 3), 3: ('y', 2, 2), 4: ('z', 1, 1)}, 9))
        self.assertEqual(ans, [('w', 4, 4), ('x', 3, 3), ('y', 2, 2)])

    def test_val_increase_weight_decrease(self):
        ans = sorted(knapsack({1: ('w', 4, 1), 2: ('x', 3, 2), 3: ('y', 2, 3), 4: ('z', 1, 4)}, 9))
        self.assertEqual(ans, [('x', 3, 2), ('y', 2, 3), ('z', 1, 4)])

    def test_val_decrease_weight_increase(self):
        ans = sorted(knapsack({1: ('w', 1, 4), 2: ('x', 2, 3), 3: ('y', 3, 2), 4: ('z', 4, 1)}, 9))
        self.assertEqual(ans, [('w', 1, 4), ('x', 2, 3), ('y', 3, 2)])


if __name__ == '__main__':
    unittest.main()