from collections import defaultdict

class Solution:
    def earliestFullBloom(self, plantTime, growTime) -> int:
        cur_plant_time, output = 0, 0

        indices = sorted(range(len(plantTime)), key=lambda x: -growTime[x])
        for i in indices:

            cur_plant_time += plantTime[i]
            output = max(output, cur_plant_time + growTime[i])

        return output




def main():
    sol = Solution()
    print(sol.earliestFullBloom(plantTime = [1,2,3,2], growTime = [1,1,1,1]))
    print(sol.earliestFullBloom(plantTime = [1,2,3,2], growTime = [1,2,3,4]))
    print(sol.earliestFullBloom(plantTime = [1,2,3,2], growTime = [4,3,2,1]))
    print(sol.earliestFullBloom(plantTime = [1,1,1,1], growTime = [1,2,3,4]))
    print(sol.earliestFullBloom(plantTime = [1,1,1,1], growTime = [4,3,2,1]))

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44")
    print(sol.earliestFullBloom(plantTime = [1,2,3,2], growTime = [2,1,2,1]))
    print(sol.earliestFullBloom([1], [1]))

if __name__ == "__main__": main()