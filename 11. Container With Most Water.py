class Solution:
    def maxArea(self, array) -> int:
        # lenght, highest, highest_position = len(array), array[0], 0
        #
        # for y in range (len(array)):
        #     if array[y] >= highest:
        #         highest=array[y]
        #         highest_position=y
        #
        # print(highest, highest_position)
        #
        # #z lava po posledny najvyssi element
        # #checkuje sa ci delta pozicii+1 je viac ako

        left , right, water = 0, len(array)-1, 0

        while left!=right:
            water = max(water, min(array[left], array[right]) * (right-left))

            if array[left]<array[right]: left+=1
            else: right-=1


        return water

def main():
    sol = Solution()
    print(sol.maxArea([0,2,1,0,1,0,1,3,2,1,2,1]))
    print(sol.maxArea([4,2,0,3,2,5]))
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == "__main__": main()