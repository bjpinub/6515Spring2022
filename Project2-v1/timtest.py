import unittest
from findX import findXinA
from GA_ProjectUtils import ExceededLookupsError, findX
import random
import math
import time


class TestFindXRepeats(unittest.TestCase):
    '''
    Unit tests for CS6515, Coding Project 2: Find x in Infinite Array.

    Author: Tim West (timwest@gatech.edu)

    This test suite is designed to ensure that the implementation
    does not rely on the assumption of unique elements. This invalid assumption
    is currently baked into the provided findX class which populates input
    A using `random.sample()`, which samples without replacement.
    '''

    def setUp(self):
        self.findXStatic = findXStatic()
        self.findX = findX()

    def test_repeat(self):
        """Find one of the valid indices for 2."""
        idx, n = findXinA(2, self.findXStatic)
        self.assertIn(idx, [2, 3])
        self.assertLessEqual(n, self.findXStatic._findXStatic__maxCalls)

    def test_repeat_2(self):
        """Find the index of 3, which appears after repeated values."""
        idx, n = findXinA(3, self.findXStatic)
        self.assertEqual(idx, 4)
        self.assertLessEqual(n, self.findXStatic._findXStatic__maxCalls)

    def test_repeat_none(self):
        """Value 5 is not in A."""
        idx, n = findXinA(5, self.findXStatic)
        self.assertEqual(idx, None)
        self.assertLessEqual(n, self.findXStatic._findXStatic__maxCalls)

    def test_repeat_none_greater(self):
        """Value 1001 is not in A and > A[n]."""
        idx, n = findXinA(1001, self.findXStatic)
        self.assertEqual(idx, None)
        self.assertLessEqual(n, self.findXStatic._findXStatic__maxCalls)

    def test_random_max_calls(self):
        """Tests 1000 random ranges for the Max Call limit."""
        diff = []
        for _ in range(1_000):
            lower = random.choice(range(1, 100))
            upper = random.choice(range(lower + 1, 100_000))
            seed = int(time.time() * 1000)
            x = random.choice(range(lower, upper))
            self.findX.start(seed, lower, upper)
            theIndex, numLookups = findXinA(x, self.findX)
            isNotPresent = x not in self.findX._findX__A[1:]  # Ignore A[0]
            if isNotPresent:
                self.assertEqual(None, theIndex, f'Expected index None. seed={seed}, nLower={lower}, nUpper={upper}')
            else:
                self.assertEqual(self.findX._findX__A[theIndex], x,
                                 f'Expected to find value {x}. seed={seed}, nLower={lower}, nUpper={upper}')
            self.assertLessEqual(numLookups, self.findX._findX__maxCalls,
                                 f'Used {numLookups} lookups, maximum={self.findX._findX__maxCalls}. seed={seed}, nLower={lower}, nUpper={upper}')
            diff.append(self.findX._findX__maxCalls - numLookups)
        print(f'Minimum remaining calls: {min(diff)}, Average remaining calls: {sum(diff) / len(diff)}')


class findXStatic():
    """Hardcoded test class with repeated elements."""

    def __init__(self):
        self.__A = [None, 1, 2, 2, 3, 4, 1000]
        self.__n = 6
        self.__lookupCount = 0
        self.__maxCalls = int(math.log(self.__n, 2) * 2) + 2
        return

    def lookup(self, i):
        self.__lookupCount += 1

        if self.__lookupCount > self.__maxCalls:
            raise ExceededLookupsError('Exceeded Maximum of {} Lookups'.format(self.__maxCalls))
        if i > self.__n:
            return None
        else:
            return self.__A[i]

    def lookups(self):
        return self.__lookupCount


if __name__ == '__main__':
    unittest.main()