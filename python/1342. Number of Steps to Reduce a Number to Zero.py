class Solution:
    def numberOfSteps(self, num: int) -> int:

        num = bin(num)
        return num.count("1") + len(num) -3

def main():
    sol = Solution()
    print(sol.numberOfSteps(8))
    print(sol.numberOfSteps(14))
    print(sol.numberOfSteps(20))
    print(sol.numberOfSteps(25))
    print(sol.numberOfSteps(123))

if __name__ == "__main__": main()


# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#
#         counter = 0
#         while num != 0:
#             if num%2 ==0: num/=2
#             else: num-=1
#
#             counter+=1
#
#         return counter