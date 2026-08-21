class Solution:

    def smallestEvenMultiple(self, n: int) -> int:
        """
            smallest=min(2,n)
            largest=max(2,n)
            multiple=0
            for i in range(1,smallest+1):
                if (largest*i)%smallest==0:
                    multiple=largest*i
                    break
            return multiple
"""
        if n%2==0:
            return n
        else:
            return n*2


                
        