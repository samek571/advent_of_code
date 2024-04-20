class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for w in words:
            #there is this problem res lib is implemented the way it starts at i+1 index not the i
            #matches = [(m.start(), m.start() + len(w) - 1) for m in re.finditer(w, text)]
            #ans.extend(matches)
            
            #done manually
            i = 0
            while i <= len(text) - len(w):
                if text[i:i+len(w)] == w:
                    ans.append([i, i+len(w)-1])
                i += 1

        return sorted(ans)
