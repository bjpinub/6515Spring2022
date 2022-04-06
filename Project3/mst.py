# -*- coding: utf-8 -*-
"""
    mst.py       Intro to Graduate Algorithms
    
    You will implement Kruskal's algorithm for finding a Minimum Spanning Tree.
    You will also implement the union-find data structure using path compression
    See [DPV] 51.3 & 5.14 for details
"""

import argparse
import GA_ProjectUtils as util

class unionFind:
    def __init__(self, n):
        self.pi = [i for i in range(n)]
        self.rank = [0 for i in range(n)]


    def areConnected(self, p, q):
        """
            return true if 2 nodes are connected or false if they are
            not by comparing their roots
        """

        if self.find(p) == self.find(q):
            return True
        else:
            return False


    def union(self, u, v):
        """
            build union of 2 components
            Be sure to maintain self.rank as needed to
            make sure your algorithm is optimal.
        """

        tmpURoot = self.find(u)
        tmpVRoot = self.find(v)

        if tmpURoot == tmpVRoot:
            return
        else:
            self.pi[tmpURoot] = tmpVRoot

    def find(self, p):
        """
            find the root of the set containing the
            passed vertex p - Must use path compression!
        """

        if self.pi[p] != p:
            self.pi[p] = self.find(self.pi[p])

        return self.pi[p]


def kruskal(G):
    """
        Kruskal algorithm
        G : graph object
    """
    #Build unionFind Object
    uf = unionFind(G.numVerts)

    #Make MST as a set
    MST = set()    

    #Get list of edges sorted by increasing weight
    sortedEdges = G.sortedEdges()   

    #Go through edges in sorted order smallest, to largest
    for e in sortedEdges:
        #TODO Your Code Goes Here (remove comments if you wish)

        tmpU, tmpV = e

        if uf.areConnected(tmpU, tmpV):
            continue
        else:
            uf.union(tmpU, tmpV)

            # use the following line to add an edge to the MST.
            # You may change it's indentation/scope within the for loop
            MST.add(util.buildMSTEdge(G,e))

        #TODone - do not modify any other code below this line
    return MST, uf

def main():
    """
    main
    """
    #DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    parser = argparse.ArgumentParser(description='Minimum Spanning Tree Coding Quiz')

    #use this flag, or change the default here to use different graph description files
    parser.add_argument('-g', '--graphFile',  help='File holding graph data in specified format', default='small.txt', dest='graphDataFileName')

    #use this flag to print the graph and resulting MST
    parser.add_argument('-p', '--print', help='Print the MSTs?', default=False, dest='printMST')

    #args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-a', '--autograde',  help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2], default=1, dest='autograde')	
    args = parser.parse_args()
    
    #DO NOT MODIFY ANY OF THE FOLLOWING CODE
    #Build graph object
    graph = util.build_MSTBaseGraph(args)
    #you may print the configuration of the graph -- only effective for graphs with up to 10 vertex
    #graph.printMe()

    #Calculate kruskal's alg for MST
    MST_Kruskal, uf = kruskal(graph)
        
    #verify against provided prim's algorithm results
    util.verify_MSTKruskalResults(args, MST_Kruskal, args.printMST)
    
if __name__ == '__main__':
    main()