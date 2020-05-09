import unittest
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        data = Counter(s)
        #print(data)
        for i,st in enumerate(s):
            if data[st]==1:
                return i
        return -1
class Test(unittest.TestCase):
    t0=[
        ("leetcode",0),
        ("loveleetcode",2)
     ]
    s=Solution()
    def test0(self):
        for testcase in self.t0:
            input, expected = testcase[0],testcase[1]
            result = self.s.firstUniqChar(input)
            self.assertEqual(result,expected)
if __name__=="__main__":
    unittest.main()