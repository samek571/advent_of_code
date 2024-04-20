import  collections

class Solution:
    def minimumRounds(self, tasks) -> int:
        hsh = collections.Counter(tasks)
        das_outputmeter_3000=0

        for val in hsh.values():
            if val == 1: return -1

            divizibel = 0 if val%3==0 else 1
            das_outputmeter_3000+= (val//3 + divizibel)

        return das_outputmeter_3000

def main():
    sol = Solution()
    print(sol.minimumRounds([2,3,3]))
    print(sol.minimumRounds([2,2,3,3,2,4,4,4,4,4]))
    print(sol.minimumRounds([2,2,2,2,2,2,2,2,2,2,2,2,2]))

if __name__ == "__main__": main()

# hsh = collections.Counter(tasks)
#
# das_outputmeter_3000=0
# for key, val in hsh.items():
#     das_outputmeter_3000+=2*(val//6)
#
#     remainder_rudolf_raindeer = val%6
#     if remainder_rudolf_raindeer in {5,4}: das_outputmeter_3000+=2
#     elif remainder_rudolf_raindeer in {2,3}: das_outputmeter_3000+=1
#     elif remainder_rudolf_raindeer == 0: das_outputmeter_3000+=0
#     elif remainder_rudolf_raindeer == 1: return -1
#
# return das_outputmeter_3000