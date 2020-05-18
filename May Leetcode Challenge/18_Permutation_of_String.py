from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1>l2:
            return False
        dct1 = Counter(s1)
        #print(dct1)
        #dct2 = Counter()
        for i in range(l2):
            if len(s2[i:i + l1]) == l1:

                dct2=Counter(s2[i:i+l1])
                #Difference is empty when all elements in s1 is present in s2
                # s1 is substring oof s2
                if dct1 - dct2 =={}:
                    return True
        return False
    #Method 2 Faster Version
    def checkInclusionMethod2(self,s1,s2):
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        dct1 = Counter(s1)
        dct2=Counter()
        for i,s in enumerate(s2):
            dct2[s]+=1
            # Sliding window while adding element to right, delete element from left
            #When the sliding window dct2 equals to dct1 return True
            if i>=l1:
                elem_from_left = s2[i-l1]
                if dct2[elem_from_left]==1:
                    del dct2[elem_from_left]
                else:
                    dct2[elem_from_left]-=1
                print("ee",elem_from_left)
            if dct2==dct1:
                return  True
        return False
s = Solution()
print(s.checkInclusion("algorithm","althmwee"))
print(s.checkInclusionMethod2("ab","sdefghab"))