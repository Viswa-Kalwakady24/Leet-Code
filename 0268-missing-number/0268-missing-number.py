class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s=0
        n=len(nums)
        totalsum=n*(n+1)//2
        for i in range(n):
            s+=nums[i]
        return totalsum-s


        