import unittest
class Solution:
    def findComplement(self, num: int) -> int:
        # return int(bin(num)[:1:-1], 2)
        temp = bin(num)[2:]
        flip = {'1': '0', '0': '1'}
        str = ''.join(flip[b] for b in temp)
        return int(str, 2)
class Test(unittest.TestCase):
    t0=[
        (5,2),
        (1,0)
     ]
    s=Solution()
    def test0(self):
        for testcase in self.t0:
            input, expected = testcase[0],testcase[1]
            result = self.s.findComplement(input)
            self.assertEqual(result,expected)
if __name__=="__main__":
    unittest.main()