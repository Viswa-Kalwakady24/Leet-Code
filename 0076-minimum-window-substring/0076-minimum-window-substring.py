class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        n=len(s)
        freq={}
        for ch in t:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        left=0
        min_len=float('inf')
        start=0
        count=0
        for right in range(n):
            if s[right]in freq:
                if freq[s[right]]>0:
                    count+=1
                    freq[s[right]]-=1
                else:
                    freq[s[right]]=-1
                while count==len(t):
                    if (right-left+1)<min_len:
                        min_len=right-left+1
                        start=left
                    if s[left] in freq:
                        freq[s[left]] += 1
                        if freq[s[left]] > 0:
                            count -= 1
                    left += 1
        if min_len==float('inf'):
            return ""
        else:
            return s[start:start+min_len]
        