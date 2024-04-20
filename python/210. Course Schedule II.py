import collections


class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph, pre_req = collections.defaultdict(set), {i:set() for i in range(numCourses)}
        for a,b in prerequisites:
            graph[b].add(a)
            pre_req[a].add(b)


        q = collections.deque([])
        for k,v in pre_req.items():
            if not v: 
                q.append(k)
        
        done = []
        while q:
            course = q.popleft()
            done.append(course)

            if len(done) == numCourses: return done

            #we have done the course --> its no longer a necesarry prerequisity
            for shit_ass_course in graph[course]:
                pre_req[shit_ass_course].remove(course)

                #therefore it can be processed (in the end everything will be processed, just now we are allowed to do so)
                if not pre_req[shit_ass_course]: q.append(shit_ass_course)


        return []


def main():
    sol = Solution()
    print(sol.fx(2, [[1,0]]))
    print(sol.fx(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(sol.fx(1, []))

if __name__ == "__main__": main()