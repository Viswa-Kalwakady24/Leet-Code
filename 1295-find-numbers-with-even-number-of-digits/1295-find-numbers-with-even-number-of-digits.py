class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            count=0
            while nums[i]>0:
                nums[i]=nums[i]//10
                count+=1
            if count%2==0:
                c+=1
        return c

        
                
        
            