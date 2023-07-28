class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):# List[List[int]]) -> List[int]:
        # alles = set()
        #
        # for x,y in edges:
        #     alles.add(y)
        #
        # output_arr=[]
        # for i in range(n):
        #     if i not in alles:
        #         output_arr.append(i)
        #
        # return output_arr

        alles = {i:0 for i in range(n)}

        for x,y in edges:
            if y in alles: alles.pop(y)

        return list(alles)





def main():
    sol = Solution()
    print(sol.findSmallestSetOfVertices(n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]))
    print(sol.findSmallestSetOfVertices(n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]))
    print(sol.findSmallestSetOfVertices(n = 2, edges = [[0,1],[1,0]]))

if __name__ == "__main__": main()