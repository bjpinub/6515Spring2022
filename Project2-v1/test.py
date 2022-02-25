import GA_ProjectUtils as util
from findX import findXinA

seeds = [123456, 12, 123, 1234, 5, 55555, 1234567890, 0, 1, 2, 3, 3683055014, 31, 700003]
indices = [10759, 50220, 923, 41939, 15580, 2267, 31815, 21848, 2980, 6096, 7840, 4700, 1237, 124]

nLower = 10
nUpper = 100000
findX = util.findX()

for seed, idx in zip(seeds, indices):
    x = findX.start(seed, nLower, nUpper)
    index, calls = findXinA(x, findX)
    if idx != index:
        print('Error on seed {}, expected index {}, got {}'.format(seed, idx, index))
    else:
        print('Seed {}: x found at index {} in {} calls'.format(seed, index, calls))

#######  x not found test cases  ##########

# special case, x below lower boundary
findX.start(1, nLower, nUpper)
index, calls = findXinA(nLower - 1, findX)
if index is not None:
    print('Failed lower boundary {}, returned {} instead of None'.format(nLower, index))

# special case, x above upper boundary
findX.start(1, nLower, nUpper)
index, calls = findXinA(nUpper + 1, findX)
if index is not None:
    print('Failed lower boundary {}, returned {} instead of None'.format(nLower, index))

# for seed=1
# findX.lookup(1) = 30
# findX.lookup(2) = 58

# special case, x below findX.lookup(1)
findX.start(1, nLower, nUpper)
index, calls = findXinA(29, findX)
if index is not None:
    print('Failed x below findX.lookup(1), returned {} instead of None'.format(index))

# special case, x between findX.lookup(1) and findX.lookup(2)
findX.start(1, nLower, nUpper)
index, calls = findXinA(57, findX)
if index is not None:
    print('Failed x between findX.lookup(1) and findX.lookup(2), returned {} instead of None'.format(index))