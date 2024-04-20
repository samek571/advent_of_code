class Solution:
    def checkIfExist(arr) -> bool:
        penis=set(arr)

        if 0 in penis:
            asdasd=arr.count(0)
            if asdasd>=2: return True

        for i in range(len(arr)):
            if (arr[i]!=0) and (arr[i]*2<=1000 and arr[i]*2>=-1000) and (arr[i]*2 in penis): return True

        return False

    print(checkIfExist([-20,8,-6,-14,0,-19,14,4])) #true
    print(checkIfExist([0,1]))
    print(checkIfExist([0,1,0]))
    print(checkIfExist([10,2,5,3]))
    print(checkIfExist([7,1,14,11]))
    print(checkIfExist([3,1,7,11]))
