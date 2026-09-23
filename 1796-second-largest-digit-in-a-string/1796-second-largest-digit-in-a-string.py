class Solution:
    def secondHighest(self, s: str) -> int:
        largest=-1
        second_largest=-1
        for i in s:
            if i.isdigit()and int(i)>largest:
                largest=int(i)
        for i in s:
            if i.isdigit()and int(i)<largest and int(i)>second_largest:
                second_largest=int(i)
        return second_largest 
        