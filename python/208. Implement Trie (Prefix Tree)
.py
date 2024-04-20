'''
its fucking obvious that we want to make a trie in which there is at most O(len(prefix))
achievable easily by inicializing set in which we insert another hashmaps if we have the urge to insert word

so basically there will be a trie with 26+1 branches at each depth storing only one letter each and every time or boolean / empty set clarifying its finished word in this depth
so like "app" will be: {a:{p:{p:{end}}}}
adding word "slut": {a:{p:{p:{end}}}, s:{l:{u:{t:{end}}}}}
adding "slot": {a:{p:{p:{end}}}, s:{l:{u:{t:{end}}, o:{t:{end}}}}}

^ best time complexity however its hard to implement for me right now
'''

class Trie:
    '''instead fuck yall this is O(worst possible)'''
    def __init__(self):
        self.massive_hsh={}
        

    def insert(self, word: str) -> None:
        self.massive_hsh[word] = 1
        

    def search(self, word: str) -> bool:
        return word in self.massive_hsh 
        

    def startsWith(self, prefix: str) -> bool:
        for i in self.massive_hsh:
            if i.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
