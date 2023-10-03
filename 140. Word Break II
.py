class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(wordDict)
        cache = {'': ['']}


        def bcktrck(s):
            if s in cache: return cache[s]
            
            cache[s] = []
            for word in wordDict:
                if s.startswith(word):
                    for possibility in bcktrck(s[len(word):]):
                        cache[s] += [word+(' '+possibility if possibility else possibility)]
            
            return cache[s]
        
        
        return bcktrck(s)
