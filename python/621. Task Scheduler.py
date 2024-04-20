import collections


class Solution:
    def leastInterval(self, tasks, n):
        freq, hsh = 0, collections.defaultdict(int)

        for i in tasks:
            hsh[i]+=1
            freq = max(freq, hsh[i])

        bazmek = (freq-1) * (n+1)

        # AAABBB 2 is basically handled, each val that is the most frequent is going to have this problem
        for val in hsh.values():
            if val == freq: bazmek+=1


        return max(bazmek, len(tasks))



def main():
    sol = Solution()
    print(sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))
    print(sol.leastInterval( ["A","A","A","B","B","B"], n = 0))
    print(sol.leastInterval(["A","A","A","B","B","B"], n = 2))

if __name__ == "__main__": main()