import unittest
class Solution():
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        row, col = len(image), len(image[0])

        oldColor=image[sr][sc]
        if oldColor == newColor:
            return image
        def dfs(r,c):
            if image[r][c]==oldColor:
                image[r][c]=newColor

                if r>=1: dfs(r-1,c)
                if r+1<row: dfs(r+1,c)
                if c>=1: dfs(r,c-1)
                if c+1<col: dfs(r,c+1)

        dfs(sr,sc)
        return image


# s=Solution()
# image = s.floodFill([[1,5,1],[1,5,5],[1,5,5]],1,2,3)
# print(image)
class Test(unittest.TestCase):
    t0=[
        ([[1,1,1],[1,1,0],[1,0,1]],1,1,2,[[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[1,5,1],[1,5,5],[1,5,5]],1,2,3,[[1, 3, 1], [1, 3, 3], [1, 3, 3]])
     ]
    s=Solution()
    def test0(self):
        for testcase in self.t0:
            input, sr,sc,newColor,expected = testcase[0],testcase[1],testcase[2],testcase[3],testcase[4]

            result = self.s.floodFill(input,sr,sc,newColor)

            self.assertEqual(result,expected)

if __name__=="__main__":

    unittest.main()