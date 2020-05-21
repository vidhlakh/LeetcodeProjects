class Solution:
    def countSquares(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        answer =[[0]*(m+1) for _ in range(n+1)]
        count =0
        for row in range(1,n+1):
            for col in range(1,m+1):
                if matrix[row-1][col-1] == 1:
                    answer[row][col] = 1+ min(answer[row][col-1], answer[row-1][col], answer[row-1][col-1])
                    count += answer[row][col]
                    print(count)
        return count
s = Solution()
matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
print(s.countSquares(matrix))
