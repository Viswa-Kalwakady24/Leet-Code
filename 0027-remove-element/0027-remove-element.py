class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        count=0
        for i in range(n):
            if nums[i]!=val:
                temp=nums[i]
                nums[i]=nums[left]
                nums[left]=temp
                count+=1
                left+=1
        return count
        