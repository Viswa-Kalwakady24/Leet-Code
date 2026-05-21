class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        parent={}
        found=False
        level=set([beginWord])
        while level and not found:
            next_level=set()
            for word in level:
                if word in wordset:
                    wordset.remove(word)
            for word in level:
                for i in range(len(word)):
                    for ch in 'qwertyuiopasdfghjklzxcvbnm':
                        new_word=word[:i]+ch+word[i+1:]
                        if new_word in wordset:
                            if new_word not in parent:
                                parent[new_word]=[]
                            parent[new_word].append(word)
                            next_level.add(new_word)
                            if new_word==endWord:
                                found=True
            level=next_level
        res=[]
        def backtrack(word,path):
            if word==beginWord:
                res.append(path[::-1])
                return
            if word not in parent:
                return 
            for p in parent[word]:
                backtrack(p,path+[p])
        if found:
            backtrack(endWord,[endWord])
        return res
            