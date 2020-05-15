class Solution:
    def numberOfArithmeticSlices(self, A):
        slices=[]
        if len(A)<3:
            return 0
        d=A[1]-A[0]
        count=0
        for i in range(1,len(A)-1):

            if A[i+1]-A[i]==d:
                for j in range(3,len(A)-2 ):

                    slices.append([A[i-1],A[i],A[i+1]])
                    count+=1
            print(slices)
    def Method2(self,A):
        if len(A) <= 2:
            return 0
        res = 0
        tmp = 0
        diff = A[1] - A[0]
        for i in range(1, len(A) - 1):
            if A[i + 1] - A[i] == diff:
                tmp += 1
                print(tmp,"temp")
            else:
                print("i=",i,"tmp",tmp)
                res += tmp * (tmp + 1) / 2
                tmp = 0
                diff = A[i + 1] - A[i]
                print(res)
        if tmp:
            print(tmp)
            res += tmp * (tmp + 1) / 2
        return res
s=Solution()
#s.numberOfArithmeticSlices([1, 3, 5, 7, 9])
print(s.Method2([1, 3, 5, 7, 9]))