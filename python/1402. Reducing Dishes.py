class Solution:
    def maxSatisfaction(satisfaction) -> int:

        # O(N logN) but it is kinda necessary for this greedy approach
        satisfaction.sort(reverse=True)
        print(satisfaction)
        if satisfaction[0]<1: return 0


        # O(n) iterating array
        satisfactory_lvl=sum_of_elements=satisfaction[0]
        i=1
        while i!= len(satisfaction):
            sum_of_elements+=satisfaction[i]

            if sum_of_elements >=0:
                satisfactory_lvl+=sum_of_elements
                i+=1
            else: return satisfactory_lvl

        return satisfactory_lvl

    print(maxSatisfaction([12]))
    print(maxSatisfaction([6,1,-8, -4, -9, -1234]))
    print(maxSatisfaction([2,4,23]))

    print("\n testestsetsetste")
    print(maxSatisfaction([-1,-8,0,5,-9]))
    print(maxSatisfaction([4,3,2]))
    print(maxSatisfaction([-1,-4,-5]))
    print(maxSatisfaction([5,3,0,-1,-2,-3]))