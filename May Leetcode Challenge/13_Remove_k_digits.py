class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        lst=list(map(int,str(num)))

        slicedList = [lst[i:len(lst)-k] for i in range(len(lst))]
        print(slicedList)
        # for elem in slicedList:
        #     lst
s=Solution()
s.removeKdigits(1432219,3)