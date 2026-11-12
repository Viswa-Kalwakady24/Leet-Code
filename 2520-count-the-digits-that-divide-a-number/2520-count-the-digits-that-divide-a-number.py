class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        s=str(num)
        for i in range(len(s)):
            digit=int(s[i])
            if digit!=0 and num%digit==0:
                count+=1
        return count