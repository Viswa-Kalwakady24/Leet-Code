class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        j=set(jewels)
        for i in range(len(stones)):
            if stones[i] in j:
                count+=1
        return count
        