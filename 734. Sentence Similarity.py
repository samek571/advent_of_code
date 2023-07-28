class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        m,n = len(sentence1), len(sentence2)
        if m != n: return False

        dick = collections.defaultdict(set)
        for a,b in similarPairs:
            dick[a].add(b)
            dick[b].add(a)
        
        for idx, word in enumerate(sentence1):
            if word != sentence2[idx]: 
                if sentence2[idx] in dick and word in dick[sentence2[idx]]: continue
                else: return False
        
        return True
