class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Using Dynamic Programming 
        # Same letter , diagonal 
        #Diff letter , min value of (left, top , diagonal ) +1
        l1 = len(word1)
        l2 = len(word2)
        result = [[0]*(l2+1) for i in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i==0:
                    result[0][j] =j
                elif j==0:
                    result[i][0] =i
                elif word1[i-1] == word2[j-1]:
                    result[i][j] = result[i-1][j-1]
                else:           # min(left,top, diagonal) +!
                    result[i][j] = min(result[i-1][j],result[i][j-1], result[i-1][j-1]) + 1
        return result[l1][l2]

s = Solution()
print(s.minDistance("Horse","Ros"))
