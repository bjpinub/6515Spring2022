# -*- coding: utf-8 -*-

"""

findX.py - Intro to Graduate Algorithms

Solve the findX in an Infinite array problem using a Divide & Conquer method
Your runtime must be O(log n)

The array of values is indexed A[1..n] inclusive

Your code MUST NOT directly reference any variables in findX.  The following methods are available:
    
    findX.start(seed) -- returns the value (x) to search for within the array
    findX.lookup(i) -- returns A[i] or None if i>n
    findX.lookups() -- returns the number of calls to lookup

""" 
#argparse allows the parsing of command line arguments
import argparse
#utility functions for cs 6515 projects
import GA_ProjectUtils as util


def findXinA(x, findX):

    #TODO Your Code Begins Here, DO NOT MODIFY ANY CODE ABOVE THIS LINE

    tmpLow = 0
    tmpHigh = 1
    tmpMid = 0
    tmpLookupVal = findX.lookup(0)

    theIndex = None # replace None with the index of x

    #Try to find the length of the array
    while tmpLookupVal is not None and tmpLookupVal < x:
        #Check if the counter happens to be the index; if it is,
        #set that it was found and break out of the loop
        if tmpLookupVal == x:
            theIndex = tmpLookupVal

            break

        #If the counter has a value and less than the x value,
        #move the low position of window up and re-adjust the high position
        tmpLow = tmpHigh
        tmpHigh = tmpHigh * 9
        tmpLookupVal = findX.lookup(tmpHigh)

    #If the x value wasn't found while trying to determine the array size,
    #work on the smaller set of data
    if theIndex is None:
        while tmpLow <= tmpHigh:
            #Print debug info
            # print(f"Lookup {findX.lookups()}:")
            # print(f"   tmpHigh: {tmpHigh}")
            # print(f"   tmpMid: {tmpMid}")
            # print(f"   tmpLow: {tmpLow}")
            # print(f"   tmpLookupVal: {tmpLookupVal}")
            # print(f"   x: {x}")

            tmpMid = tmpLow + (tmpHigh - tmpLow) // 2

            tmpLookupVal = findX.lookup(tmpMid)

            if tmpLookupVal == x:
                theIndex = tmpMid

                break

            if tmpLookupVal is None or tmpLookupVal > x:
                tmpHigh = tmpMid - 1
            else:
                tmpLow = tmpMid + 1

    #TODOne Your code Ends here, DO NOT MOIDFY ANYTHING BELOW THIS LINE

    numLookups = findX.lookups()

    return theIndex, numLookups


def main():
    """
    main - DO NOT CHANGE ANYTHING BELOW THIS LINE
    """
    # DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    parser = argparse.ArgumentParser(description='Find X Coding Quiz')

    #args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-a', '--autograde',  help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2], default=1, dest='autograde')
    parser.add_argument('-s', '--seed', help='seed value for random function', type=int, default=123456, dest='seed')
    parser.add_argument('-l', '--nLower', help='lower bound for N', type=int, default=10, dest='nLower')
    parser.add_argument('-u', '--nUpper', help='upper bound for N', type=int, default=100000, dest='nUpper')

    args = parser.parse_args()

    #DO NOT MODIFY ANY OF THE FOLLOWING CODE

    findX = util.findX()
    x = findX.start(args.seed, args.nLower, args.nUpper)
    index, calls = findXinA(x, findX)
    print('findX result: x found at index {} in {} calls'.format(index, calls))

    return

if __name__ == '__main__':
    main()