class Solution:
    # def checker(self, a,b):
    #
    #     if a==b: return True
    #     if a>

    def asteroidCollision(self, asteroids):# List[int]) -> List[int]:

        stck = []
        for num in asteroids:
            while stck and stck[-1]>0 and num < 0:
                if stck[-1] + num < 0: stck.pop()
                elif -num == stck[-1]: stck.pop() ; break
                else: break

            else: stck.append(num)

        return stck
        #     # the only way we encounter a collision
        #     elif stck[-1] > 0 and num < 0:
        #         if stck[-1] == -num: stck.pop()
        #
        #         elif abs(stck[-1]) < abs(num):
        #             while stck and ((abs(stck[-1]) < abs(num) and stck[-1]>0) or ):
        #                 stck.pop()
        #
        #             if not stck or (stck[-1]>0 and num>0) or (stck[-1]<0 and num<0):
        #                 stck.append(num)
        #
        #
        #     else:stck.append(num)
        # return stck


def main():
    sol = Solution()
    print(sol.asteroidCollision([-2,2,1,-2]))
    print(sol.asteroidCollision([2,1]))
    print(sol.asteroidCollision([2,-1]))
    print(sol.asteroidCollision([-2,1]))
    print(sol.asteroidCollision([-2,-1]))
    print(sol.asteroidCollision([1,-2]))
    print(sol.asteroidCollision([1,2]))
    print(sol.asteroidCollision([-1,2]))
    print(sol.asteroidCollision([-1,-2]))
    print(sol.asteroidCollision([10,-5,-11, 7, -4, -8, 14, 2, 15, -90])) #-11 -8 -90
    print(sol.asteroidCollision([-11, 15, -90])) #-11 -90
    print(sol.asteroidCollision([16, -15, 90])) #16 90
    print(sol.asteroidCollision([10,-5,-11, 7, -4, -8, 14, 2, 15, -9])) #-11 -8 14 2 15
    print(sol.asteroidCollision([5,10,-5,-11, 7, -4, -8])) #-11 -8
    print(sol.asteroidCollision([5,10,-5,-11, 7, -4])) #-11 7
    print("ASDADADS")
    print(sol.asteroidCollision([5,10,-5])) #5 10
    print(sol.asteroidCollision([8,-8]))  #
    print(sol.asteroidCollision([10,2,-5])) #10

if __name__ == "__main__": main()
