from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dct ={}
        result =''
        for i in s:
            if i in dct:
                dct[i]+=1
            else:
                dct[i] = 1
        sorted_lst = sorted(dct , key= lambda x: dct[x], reverse=True)
        for char in sorted_lst:
            result+= char * dct[char]
        return result



s = Solution()
s.frequencySort("ttttreessscc")
s.frequencySort("cccaaa")
s.frequencySort("Aabb")