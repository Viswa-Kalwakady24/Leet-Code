class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        while n>0:
            digit=n%10
            s+=digit
            p*=digit
            n=n//10
        return p-s
            
        