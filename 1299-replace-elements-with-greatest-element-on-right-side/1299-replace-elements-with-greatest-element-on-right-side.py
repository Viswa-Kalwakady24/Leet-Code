class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_num=-1
        for i in range(len(arr)-1,-1,-1):
            curr=arr[i]
            arr[i]=max_num
            if curr>max_num:
                max_num=curr
        return arr