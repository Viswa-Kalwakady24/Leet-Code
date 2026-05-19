class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_word=set(nums)
        if len(nums)==len(new_word):
            return False
        else:
            return True
        