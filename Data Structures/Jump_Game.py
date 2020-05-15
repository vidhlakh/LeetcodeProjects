class Solution:
    def canJump(self, nums):
        size = len(nums)
        #current_index = 1
        #for i, n in enumerate(nums):
        i=0
        cur_index=1
        if size<=2:
            return True
        while(i<size):
            if  nums[i]<size:
                if i==size-1:
                    return True
                i += nums[i]
                print(i)
                return False
    # def canJumpMethod2(self,nums):
    #     if (nums.length == 0):
    #         return False
    #
    #     farthest = 0
    #     for (int i = 0; i <= farthest & & i < nums.length; ++i):
    #         farthest = Math.max(farthest, i + nums[i]);
    #     }
    #     return farthest >= nums.length - 1;

s= Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))