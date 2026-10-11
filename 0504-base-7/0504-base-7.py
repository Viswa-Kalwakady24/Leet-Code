class Solution:
    def convertToBase7(self, num: int) -> str:
        s=""
        x=abs(num)
        if x==0:
            s="0"
        while x>0:
            s=str(x%7)+s
            x=x//7
        if num<0:
            s="-"+s
        return s