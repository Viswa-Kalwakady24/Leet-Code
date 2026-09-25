class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        negative=x<0
        if x<0:
            x=abs(x)
        while x:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if negative:
            rev=-rev
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev

        