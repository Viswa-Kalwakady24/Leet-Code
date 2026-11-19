class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("aeiouAEIOU")
        c=list(s)
        left=0
        right=len(c)-1
        while left<right:
            if c[left] not in vowels:
                left+=1
            elif c[right] not in vowels:
                right-=1
            else:
                c[left],c[right]=c[right],c[left]
                left+=1
                right-=1
        return "".join(c)
        