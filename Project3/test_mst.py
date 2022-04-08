import GA_ProjectUtils as util
import unittest
from mst import kruskal

# Add the names of the tests you want to run to this list (make sure you have both the input and the solution files)
test_cases = ["small.txt", "medium.txt", "mst_5.1.txt",
              "mst_5.2.txt", "1000EWG.txt", "10000EWG.txt", "test_1.txt", "test_2.txt", "test_3.txt"]


class Project3Test(unittest.TestCase):
    """
    Test suite for CS 6515, Coding Project 3

    Tests collected from https://edstem.org/us/courses/16028/discussion/1352419 and put together by Thinh Cao (tcao44@gatech.edu)

    I assume no responsibility for the correctness or completeness of this test suite. Please use at your own risk.
    """

    def __load_correct_MST(self, test_name):
        """Load the correct MST from solution file
        """
        solution_name = f"soln_{test_name}"
        result_data_list = util.readFileDat(solution_name)
        MST = set()
        for line in result_data_list:
            vals = line.split()
            v1 = int(vals[0].strip())
            v2 = int(vals[1].strip())
            wt = float(vals[2].strip())
            MST.add((wt, (v1, v2)))
        return MST

    def __verify_MST(self, returned_MST, correct_MST):
        """Verify if your MST is correct
        """
        returned_MST_weight = round(
            util.findTotalWeightOfMst(returned_MST), 12)
        correct_MST_weight = round(util.findTotalWeightOfMst(correct_MST), 12)
        return abs(returned_MST_weight - correct_MST_weight) < 1e-12

    def __run_test(self, test_name):
        MSTGraphData = util.readFileDat(test_name)
        numVerts = int(MSTGraphData[0].strip())
        numEdges = int(MSTGraphData[1].strip())
        edgeDataAra = []
        for i in range(numEdges):
            line = MSTGraphData[i+2]
            vals = line.split()
            v1 = int(vals[0].strip())
            v2 = int(vals[1].strip())
            wt = float(vals[2].strip())
            edgeDataAra.append([wt, v1, v2])

        graph = util.Graph(numVerts, edgeDataAra)
        MST_Kruskal, _ = kruskal(graph)
        correct_MST = self.__load_correct_MST(test_name=test_name)
        return self.__verify_MST(MST_Kruskal, correct_MST)

    def test_MST(self):
        for test_case in test_cases:
            with self.subTest(msg=f"Test: {test_case}"):
                assert self.__run_test(test_case)


if __name__ == "__main__":
    unittest.main()
