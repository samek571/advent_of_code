class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        if endWord not in wordList or not endWord or not beginWord or not wordList: return 0
        

        #makes from "hope" all possibilities that could be located in wordlist as adjecent
        # #ope h#pe ho#e hop#
        similarities = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                similarities[word[:i] + "#" + word[i+1:]] += [word]
        

        #bfs since we want the shortest path from a to b
        q = collections.deque([(beginWord, 1)]) #word and the number of change
        visited = set()
        while q:
            curr, lvl = q.popleft()
            for idx in range(n):
                possible = curr[:idx] + "#" + curr[idx+1:]

                for nxt in similarities[possible]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, lvl+1))

                        if nxt == endWord: return lvl+1
                
                del similarities[possible] #faster searching time for others

        return 0 #in case its already the endword
