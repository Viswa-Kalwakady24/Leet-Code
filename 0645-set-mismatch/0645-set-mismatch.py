class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        duplicate=0
        missing=0
        #duplicate
        for i in nums:
            if i in s:
                duplicate=i
            else:
                s.add(i)
        #missing
        for i in range(1,len(nums)+1):
            if i not in s:
                missing=i
        return [duplicate,missing]
        