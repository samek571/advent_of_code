import collections

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        def dfs(node, seen):
            if node in seen: return node
            seen.add(node)

            #since its not gonna be modified no more, there is no need to pass it to each dfs
            nonlocal graph

            letter = node
            for element in graph[node]:
                letter = min(letter, dfs(element, seen))

            return letter


        graph = collections.defaultdict(list)
        for x, y in zip(s1, s2):
            graph[x].append(y)
            graph[y].append(x)

        print(graph)
        o=''
        # we actually need to do dfs since its a graph, meaning covering the only adjecent nodes is not enough
        for letter in baseStr:

            o+= dfs(letter, set())

        return o



def main():
    sol = Solution()
    print(sol.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))
    print(sol.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold"))
    print(sol.smallestEquivalentString("leetcode", s2 = "programs", baseStr = "sourcecode"))

if __name__ == "__main__": main()

# graph = collections.defaultdict(list)
# for x, y in zip(s1, s2):
#     graph[x].append(y)
#     graph[y].append(x)
#
# for letter in baseStr:
#     graph[letter].append(letter)
#
# print(graph)
# o = ''
# for letter in baseStr:
#     o += min(graph[letter])
#
# return o