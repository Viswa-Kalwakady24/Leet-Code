class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected=sorted(heights)  # sorted()-> sorts and creates new list
        #.sort()-> sorts in the list itself
        count=0
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                count+=1
        return count
        