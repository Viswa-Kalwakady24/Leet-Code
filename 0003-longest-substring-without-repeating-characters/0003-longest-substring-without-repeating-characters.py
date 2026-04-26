class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        max_len=0
        character_set=set()
        for right in range(n):
            if s[right] not in character_set:
                character_set.add(s[right])
                max_len=max(max_len,right-left+1)
            else:
                while s[right] in character_set:
                    character_set.remove(s[left])
                    left+=1
                character_set.add(s[right])
        return max_len
        