#Uncrossed lines similar to Longest subsequence 
class Solution:
    def maxUncrossedLines(self, A, B):
        n_rows = len(A)
        n_cols = len(B)
        result = [[0]*(n_cols+1) for  i in range(n_rows+1)]

        for row in range( len(A)):
            for col in range(len(B)):
                if A[row] == B[col]:
                    result[row+1][col+1] = 1+ result[row][col]

                else:
                    result[row+1][col+1] = max(result[row+1][col],result[row][col+1])

        return (result)




s = Solution()
print(s.maxUncrossedLines([1,4,2],[1,2,4]))
print(s.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))
#Table using Dynamic Programming
#		1	2	4
#0	0	0	0	0
#1	0	1 (if match, diagonal +1)	1 no match , max (row-1,col,row,col-1)	1 no match max(row-1,col,row,col-1)
#4	0	1 no match , max (row-1,col,row,col-1)	1 no match , max (row-1,col,row,col-1)	2 (if match, diagonal +1)
#2	0	1 no match , max (row-1,col,row,col-1)	2 (if match, diagonal +1)	2 no match , max (row-1,col,row,col-1)
