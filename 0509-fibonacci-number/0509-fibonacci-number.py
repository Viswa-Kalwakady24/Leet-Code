class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        c=0
        while c<n:
            next=a+b
            c+=1
            a=b
            b=next
        return a
        