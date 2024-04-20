class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = collections.deque()
        q.append(0)
        visited = [False]*len(rooms)
        visited[0]=True

        while q:
            node = q.popleft()
            for adj in rooms[node]:
                if not visited[adj]:
                    visited[adj]=True
                    q.append(adj)

        return all(visited)
