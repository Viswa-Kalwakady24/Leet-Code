class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        total = 0
        ans = []
        for i in nums:
            total += i
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            diff = abs(left_sum - right_sum)
            ans.append(diff)
            left_sum += nums[i]
        return ans
