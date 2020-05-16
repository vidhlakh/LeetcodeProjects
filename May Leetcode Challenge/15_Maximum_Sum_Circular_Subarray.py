
class Solution:
    def kadane(self, array):

        local_sum,global_sum=array[0],array[0]
        for i in range(1, len(array)):
            local_sum = max(array[i], local_sum + array[i])
            global_sum = max(local_sum,global_sum)
        return global_sum
    def maxSubarraySumCircular(self, A):


        k=self.kadane(A)

        new_A = [-1*i for i in A]
        cs = sum(A)
        cs = cs+self.kadane(new_A)
        if cs>k and cs!=0:
            print(cs)
        else:
            print(k)

s = Solution()
s.maxSubarraySumCircular([1,-2,3,-2])
s.maxSubarraySumCircular([5,-3,5])
s.maxSubarraySumCircular([3,-2,2,-3])
s.maxSubarraySumCircular([-2,-3,-1])
