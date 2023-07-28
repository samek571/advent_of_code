from collections import defaultdict

class Solution:
    def maxOperations(self, nums, target: int) -> int:
        dick = defaultdict(int)

        for i in nums:
            dick[i]+=1

        decreased=0
        tupled_dick = dick
        for key in dick.keys():
            opposite = target-key

            if opposite in dick and key in dick and key<=target//2:
                if opposite != key:
                    decreased += min(tupled_dick[key], tupled_dick[opposite])

                else:
                    decreased += tupled_dick[key]//2

        return decreased





def main():
    sol = Solution()
    print(sol.maxOperations([3,1,3,4,3,5], target = 6))
    print(sol.maxOperations([3,1,3,4,3], target = 6))
    print(sol.maxOperations([1,2,3,4], 5))
    print(sol.maxOperations([1], 5))
    print(sol.maxOperations([1,4], 5))

if __name__ == "__main__": main()