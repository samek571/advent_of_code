class Solution:
    def canFinish(self, numCourses: int, nums: List[List[int]]) -> bool:
        #made one directed graph
        graph = collections.defaultdict(list)
        for i in range(numCourses):
            graph[i] = []

        for a,b in nums:
            graph[a].append(b)
        

        visited = set()
        def dfs(course):
            if course in visited: return False
            if course not in graph: return True

            visited.add(course)
            for req in graph[course]:
                if not dfs(req): return False
            visited.remove(course)

            del graph[course]
            return True
        

        for course in range(numCourses):
            # if there is one cycle, anywhere
            if not dfs(course): return False
        
        return True
