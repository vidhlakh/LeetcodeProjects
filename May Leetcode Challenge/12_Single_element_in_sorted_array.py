from  collections import Counter
import unittest
class Solution:
    def singleNonDuplicate(self, nums):
        dct = Counter(nums)
        print([k for k,v in dct.items() if v==1])

s = Solution()
s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
class Test(unittest.TestCase):
    t0=[
        ([1,1,2,3,3,4,4,8,8],2),
        ([3,3,7,7,10,11,11],10)
     ]
    s=Solution()
    def test0(self):
        for testcase in self.t0:
            input, expected = testcase[0],testcase[1]

            result = self.s.checkStraightLine(input)
            self.assertEqual(result,expected)
if __name__=="__main__":
    unittest.main()