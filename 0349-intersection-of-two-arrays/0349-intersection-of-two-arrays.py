class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in s:
                    s.append(nums1[i])
        return s