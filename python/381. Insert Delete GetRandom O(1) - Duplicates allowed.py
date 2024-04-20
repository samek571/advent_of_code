from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.mydick = defaultdict(set)


    def insert(self, val: int) -> bool:

        self.mydick[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.mydick[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.mydick[val]: return False

        remove, last = self.mydick[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.mydick[last].add(remove)
        self.mydick[last].discard(len(self.lst) - 1)

        self.lst.pop()
        return True


    def getRandom(self) -> int:
        return choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
def main():
    sol = RandomizedCollection()
    sol.insert(1)
    sol.insert(1)
    sol.remove(1)
    sol.getRandom()

if __name__ == "__main__": main()

    # def __init__(self):
    #     self.mydick = defaultdict(int)
    #
    # def insert(self, val: int) -> bool:
    #     boool = val not in self.mydick
    #
    #     self.mydick[val]+=1
    #     return boool
    #
    # def remove(self, val: int) -> bool:
    #     if val in self.mydick:
    #         self.mydick[val]-=1
    #         if self.mydick[val] == 0: self.mydick.pop(val)
    #         return True
    #
    #     return False
    #
    # def getRandom(self) -> int:
    #     mylist = []
    #     for key, val in self.mydick.items():
    #         mylist += [key]*val
    #
    #     return random.choice(mylist)