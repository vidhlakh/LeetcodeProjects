import unittest
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num**(1/2)).is_integer():
            return True
        else:
            return False

    def isPerfectSquareMethod2(self, num: int) -> bool:
        if num < 2:
            return True
        left = 2
        right = num // 2
        while (left <= right):
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid - 1
        return False
class Test(unittest.TestCase):
    t0=[
        (16,True),
        (14,False)
     ]
    s=Solution()
    def test0(self):
        for testcase in self.t0:
            input, expected = testcase[0],testcase[1]

            result = self.s.isPerfectSquare(input)
            result2 = self.s.isPerfectSquareMethod2(input)
            self.assertEqual(result,expected)
            self.assertEqual(result2, expected)
if __name__=="__main__":

    unittest.main()