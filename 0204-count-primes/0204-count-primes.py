class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        primes=[1]*n
        i=2
        while i*i<n:
            if primes[i]==1:
                for j in range(i*i,n,i):
                        primes[j]=0
            i+=1
        return primes.count(1)-2