class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_count=0
        for i in sentences:
            w=i.split()
            if len(w)>max_count:
                max_count=len(w)
        return max_count