import GA_ProjectUtils as util
from findX import findXinA

if __name__ == '__main__':  # small test suite for testing edge cases
    findX = util.findX()

    # tight case 1 (None)
    target_x = findX.start(1200652955, 1, 6)
    index, calls = findXinA(57, findX)
    if index is not None:
        print('Failed!')
    else:
        print('Passed!')

    # tight case 2
    target_x = findX.start(1200652955, 1, 6)  # A =  [-, 2, 4, 5, 8, 10]
    index, calls = findXinA(10, findX)
    if index != 5:
        print(f'Failed! with return index {index}')
    else:
        print('Passed!')