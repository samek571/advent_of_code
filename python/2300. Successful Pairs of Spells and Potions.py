
class Solution:
    # sort potions and by iteration of spells do binary search which first potion does more than success in product
    # and return retrun n-i or some

    def bs(self, potions, success, spell):
        potion_needed = (success + spell - 1) // spell
        l, r = 0, len(potions)
        while l < r:
            mid = l + (r - l) // 2
            if potions[mid] >= potion_needed:
                r = mid
            else:
                l = mid + 1
        return l


    def successfulPairs(self, spells, potions, success: int):
        potions.sort() ; o = [] ; n = len(potions)

        for i in spells:
            o.append(n-self.bs(potions, success, i))

        return o


def main():
    sol = Solution()
    print(sol.successfulPairs([3,1,2], potions = [8,5,8], success = 16))
    print(sol.successfulPairs([5,1,3], potions = [1,2,3,4,5], success = 7))
    #print(sol.successfulPairs())

if __name__ == "__main__": main()
