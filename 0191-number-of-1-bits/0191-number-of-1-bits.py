class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n).count('1')
        return b
        