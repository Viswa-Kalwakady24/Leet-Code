class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        left=0
        freq={}
        max_freq=0
        ans=0
        for right in range(n):
            if s[right]in freq:
                freq[s[right]]+=1
            else:
                freq[s[right]]=1
            max_freq=max(max_freq,freq[s[right]])
            while (right -left + 1) - max_freq > k:
                freq[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans