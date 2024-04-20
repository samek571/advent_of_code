class Solution:
    def minimumCardPickup(self, cards) -> int:
        hsh = dict()

        output = float('inf')
        for i, card in enumerate(cards):
            if card in hsh:
                output = min(i- hsh[card]+1, output)

            hsh[card]=i

        if output == float('inf'): return -1
        return output

def main():
    sol = Solution()
    print(sol.minimumCardPickup([3,4,2,3,4,7]))
    print(sol.minimumCardPickup([1,0,5,3]))
    print(sol.minimumCardPickup([1,0,5,3,1, 2, 8, 2]))
    print(sol.minimumCardPickup([1,0,5,3,1]))
    print(sol.minimumCardPickup([1,0,5,3,1,2,2]))

if __name__ == "__main__": main()