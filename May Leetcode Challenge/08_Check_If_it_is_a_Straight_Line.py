import numpy as np

import unittest
class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True
        npdata = np.array(coordinates)

        for i in range(len(npdata) - 2):
            AB = np.cross(npdata[i], npdata[i + 1])
            BC = np.cross(npdata[i + 1], npdata[i + 2])
            AC = np.cross(npdata[i], npdata[i + 2])
            if AC == AB + BC:
                label = True
                continue
            else:
                label = False
                break
        return label
class Test(unittest.TestCase):
    t0=[
        ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],True),
        ([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]],False)
     ]
    s=Solution()
    def test0(self):
        for testcase in self.t0:
            input, expected = testcase[0],testcase[1]

            result = self.s.checkStraightLine(input)
            self.assertEqual(result,expected)
if __name__=="__main__":
    unittest.main()