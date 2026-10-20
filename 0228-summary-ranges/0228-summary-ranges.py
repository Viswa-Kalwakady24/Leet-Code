class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        start=0
        res=[]
        for i in range(1,len(nums)):
                if nums[i]!=nums[i-1]+1:
                    if start==i-1:
                        res.append(str(nums[start]))
                    else:
                        res.append(str(nums[start])+"->"+str(nums[i-1]))
                    start=i
        if start==len(nums)-1:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start])+"->"+str(nums[-1]))
        return res
        