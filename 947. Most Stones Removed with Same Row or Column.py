class Solution:
	def removeStones(self, stones) -> int:

		def dfs(i,j):
			gathered = []
			ind = 0
			while ind < len(stones):
				x,y = stones[ind]
				if x == i or y == j:
					gathered.append(stones.pop(ind))
				else:
					ind += 1
			for stone in gathered:
				dfs(*stone)

		ans = len(stones)
		while stones:
			dfs(*stones.pop())
			ans -= 1
		return ans

def main():
    sol = Solution()
    print(sol.removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))

if __name__ == "__main__": main()