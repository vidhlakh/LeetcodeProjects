import unittest
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        maj = len(nums) // 2
        dct = Counter(nums)

        for k, v in dct.items():
            if v > maj:
                return k
class Test(unittest.TestCase):
    t0=[
        ([3,2,3],3),
        ([2,2,1,1,1,2,2],2)
     ]
    s=Solution()
    def test0(self):
        for testcase in self.t0:
            input, expected = testcase[0],testcase[1]
            print(input,type(input))
            result = self.s.majorityElement(input)
            self.assertEqual(result,expected)
if __name__=="__main__":
    unittest.main()