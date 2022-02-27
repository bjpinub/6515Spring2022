import GA_ProjectUtils as util
from findX import findXinA
import findX
import random
import math
from cmath import inf
from numpy import Inf
from datetime import datetime


def search(a, len, x):
    for index in range(1, len + 1):

        if (a[index] == x):
            # Return index where x is found
            return index

    return None


if __name__ == '__main__':

    findX = util.findX()

    ############# Original test cases ##########################
    print('-----------------------------------------------------------------------------------')
    seeds = [123456, 12, 123, 1234, 5, 55555, 1234567890, 0, 1, 2, 3, 3683055014, 31, 700003]
    indices = [10759, 50220, 923, 41939, 15580, 2267, 31815, 21848, 2980, 6096, 7840, 4700, 1237, 124]

    nLower = 10
    nUpper = 100000

    for seed, idx in zip(seeds, indices):
        x = findX.start(seed, nLower, nUpper)
        index, calls = findXinA(x, findX)
        if idx != index:
            print('Error on seed {}, expected index {}, got {}'.format(seed, idx, index))
        else:
            print('Seed {}: x found at index {} in {} calls'.format(seed, index, calls))

    print(
        '--------------------------------------------------------------------------------------------------------------')

    ############ Broader tests that also test small array sizes ###################
    num_tests = 200
    random.seed(datetime.now())
    seeds = random.sample(range(1234567890), num_tests + 10)

    nLower_reduce = 10
    nUpper_reduce = 1000
    nLower = nLower_reduce * num_tests
    nUpper = nUpper_reduce * num_tests

    total_call_diff = 0
    min_call_diff = nUpper
    max_call_diff = 0
    for seed in seeds:
        x = findX.start(seed, nLower, nUpper)
        index, calls = findXinA(x, findX)
        answer_index = search(findX._findX__A, findX._findX__n, x)
        call_diff = findX._findX__maxCalls - calls
        min_call_diff = min(min_call_diff, call_diff)
        max_call_diff = max(max_call_diff, call_diff)
        total_call_diff += call_diff
        if index != answer_index:
            print('Error on seed {}, lbound {}, ubound {}, expected index {}, got {}'.format(seed, nLower, nUpper,
                                                                                             answer_index, index))
        else:
            print(
                'Seed {}, lbound {}, ubound {}: x found at index {} in {} calls (remaining calls = {} / max calls = {})'.format(
                    seed, nLower, nUpper, index, calls, call_diff, findX._findX__maxCalls))

            # Reduce upper / lower bounds
        if (nUpper > 10):
            nUpper = max(10, nUpper - nUpper_reduce)
        else:
            nUpper = max(1, nUpper - 1)
        if (nLower > 5):
            nLower = max(5, nLower - nLower_reduce)
        else:
            nLower = max(1, nLower - 1)

    print('Average remaining calls {}, min remaining calls {}, max remaining calls {}'.format(
        total_call_diff / (len(seeds)), min_call_diff, max_call_diff))
    print(
        '--------------------------------------------------------------------------------------------------------------')

    ########################## X not Found Test Cases #########################

    # Reset lower / upper bounds for not found cases
    nLower = 10
    nUpper = 100000

    # special case, x below lower boundary
    findX.start(1, nLower, nUpper)
    index, calls = findXinA(nLower - 1, findX)
    if index is not None:
        print('Failed x={} below lower boundary {}, returned {} instead of None'.format(nLower - 1, nLower, index))
    else:
        print('Passed x={} below lower boundary {}, returned None'.format(nLower - 1, nLower))

    # special case, x above upper boundary
    findX.start(1, nLower, nUpper)
    index, calls = findXinA(nUpper + 1, findX)
    if index is not None:
        print('Failed x={} above upper boundary {}, returned {} instead of None'.format(nUpper + 1, nUpper, index))
    else:
        print('Passed x={} above upper boundary {}, returned None'.format(nUpper + 1, nUpper))

    # special case, x below findX.lookup(1)
    findX.start(1, nLower, nUpper)
    index, calls = findXinA(29, findX)
    if index is not None:
        print('Failed x below findX.lookup(1), returned {} instead of None'.format(index))
    else:
        print('Passed x below findX.lookup(1), returned None')

    # special case, x between findX.lookup(1) and findX.lookup(2)
    findX.start(1, nLower, nUpper)
    index, calls = findXinA(57, findX)
    if index is not None:
        print('Failed x between findX.lookup(1) and findX.lookup(2), returned {} instead of None'.format(index))
    else:
        print('Passed x between findX.lookup(1) and findX.lookup(2), returned None')
    print(
        '--------------------------------------------------------------------------------------------------------------')