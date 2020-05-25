class Solution:
    def intervalIntersection(self, A, B):
        i,j=0,0
        intervals =[]
        while (i< len(A) and j < len(B) ):
            #Starting point is maximum of both the points, Ending is minimum of both the points
            interval_starting, interval_ending = max(A[i][0], B[j][0]), min(A[i][1],B[j][1])
            if interval_starting <= interval_ending:
                intervals.append([interval_starting,interval_ending])
            if A[i][1] < B[j][1]:
                i +=1 # if A's ending element is lesser, increemnts A's ending to next staritng eleemnt
            else:
                j +=1
        return intervals



s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))