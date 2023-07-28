from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        # target 1 splits into 2 separate ways of A and R at every new number -->
        # bfs from 1 to target and return the path first encountered path

        q = deque([(0,0,1)])
        while q:
            move, pos, vel = q.popleft()
            if pos == target: return move

            q.append((move+1, pos+vel, vel*2))

            if (pos > target and vel > 0) or (pos < target and vel < 0) or\
                    (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                q.append((move + 1, pos, -1 if vel > 0 else 1))


def main():
    sol = Solution()
    print(sol.racecar(9))
    print(sol.racecar(11))
    print(sol.racecar(523))
    print(sol.racecar(2112))

if __name__ == "__main__": main()