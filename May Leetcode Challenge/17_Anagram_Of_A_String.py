from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        s_len,p_len = len(s),len(p)
        if s_len<p_len:
            return []
        p_count = Counter(p)
        s_count = Counter()
        result=[]
        for i in range(s_len):
            s_count[s[i]]+=1
            if i>=p_len:
                if s_count[s[i-p_len]] ==1:
                    del s_count[s[i-p_len]]
                else:
                    s_count[s[i-p_len]]-=1
            if p_count==s_count:
                result.append(i-p_len +1)
        return result
s=Solution()
print(s.findAnagrams("abcd","ab"))