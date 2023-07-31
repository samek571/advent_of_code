'''Classic Trie problem - use hashmaps; lists could be presorted so the insertion is lgn and ls in o(1)'''
from collections import defaultdict
from typing import List

class FileSystem:
    def __init__(self):
        Trie = lambda: collections.defaultdict(Trie)
        self.root = Trie()

    #iterative dfs helper to get to the appropriate folder
    def _traverse_path(self, path: str):
        actual = self.root
        for word in filter(None, path.split('/')):
            actual = actual[word]
        return actual



    def ls(self, path: str) -> List[str]:
        actual = self._traverse_path(path)
        if 'blabla' in actual:
            return [path.split('/')[-1]]
        else:
            return sorted(actual.keys())

    def mkdir(self, path: str) -> None:
        self._traverse_path(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        actual = self._traverse_path(filePath)
        if 'blabla' not in actual:
            actual['blabla'] = ''
        actual['blabla'] += content

    def readContentFromFile(self, filePath: str) -> str:
        actual = self._traverse_path(filePath)
        return actual['blabla']
