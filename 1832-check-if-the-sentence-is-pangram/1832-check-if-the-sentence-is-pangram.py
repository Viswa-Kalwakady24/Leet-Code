class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set()
        for i in range(len(sentence)):
            if sentence[i] not in s:
                s.add(sentence[i])
        if len(s)==26:
            return True
        else:
            return False
        