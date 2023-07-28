class Solution:
    def duplicateZeros(arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i<len(arr)-1:
            if arr[i]==0:
                arr.insert(i, 0)
                arr.pop()
                i+=1
            i+=1

        return arr


    print(duplicateZeros([1,0,2,3,0,4,5,0]))
    print(duplicateZeros([1,2,0,3]))
    print(duplicateZeros([0,0,0]))
    print(duplicateZeros([1]))

        # i=0
        # while i<len(arr)-1:
        #     if arr[i]==0:
        #         first=arr[:i]
        #         second=arr[i:-1]
        #         arr=first + [0] + second
        #         i+=1
        #     i+=1
        #
        # return arr

        # i=0
        # while i<len(arr)-1:
        #
        #     if arr[i]==0:
        #         arr=arr[:i]+[0]+arr[i:-1]
        #         i+=2
        #         continue
        #     i+=1
        #
        # return arr

