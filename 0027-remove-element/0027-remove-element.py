class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        n=len(nums)
        left=0
        count=0
        for i in range(n):
            if nums[i]!=val:
                temp=nums[i]
                nums[i]=nums[left]
                nums[left]=temp
                count+=1
                left+=1
        return count
        '''
        left=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[left]=nums[i]
                left+=1
        return left