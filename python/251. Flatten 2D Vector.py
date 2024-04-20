import collections
import re

class Vector2D:

    def __init__(self, vec: list[list[int]]):
        self.vec = vec
        f = [num for sublist in self.vec for num in sublist]
        #self.arr = collections.deque(re.match("\d+", str(self.vec)))
        self.arr = collections.deque(f)

    def next(self) -> int:
        return self.arr.popleft()

    def hasNext(self) -> bool:
        return len(self.arr) > 0

def main():
    obj = Vector2D(["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"])
    print(obj.arr)

if __name__ == "__main__": main()
