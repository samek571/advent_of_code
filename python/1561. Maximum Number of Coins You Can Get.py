class Solution:
    def maxCoins(piles) -> int:
        piles.sort(reverse=True)

        counter=0
        i=1
        while i<=(len(piles)*2/3):
            counter+=piles[i]
            i+=2
        return counter

    print(maxCoins([9,8,7,6,5,4,3,2,1,1,1,1]))
    print(maxCoins([2,4,1,2,7,8]))
    print(maxCoins([1,2,9]))