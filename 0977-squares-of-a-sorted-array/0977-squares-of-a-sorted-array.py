class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        res=[]
        for i in nums:
            s=i*i
            res.append(s)
            res.sort()
        return res
'''
        n=len(nums)
        left=0
        right=n-1
        position=n-1
        res=[0]*n
        while left<=right:
                if abs(nums[left])<abs(nums[right]):
                    res[position]=nums[right]*nums[right]
                    right-=1
                    position-=1
                else:
                    res[position]=nums[left]*nums[left]
                    left+=1
                    position-=1
                
        return res



        