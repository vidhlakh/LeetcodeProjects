class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        jew = set(J)
        for stone in S:
            if stone in jew:
                count+=1
        return count