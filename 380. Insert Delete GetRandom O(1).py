import random
class RandomizedSet:

    def __init__(self):
        self.mydick = {}

    def insert(self, val: int) -> bool:
        if val not in self.mydick:
            self.mydick[val]=1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.mydick:
            self.mydick.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.mydick.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def main():
    sol = RandomizedSet()
    print(sol.getRandom())

if __name__ == "__main__": main()