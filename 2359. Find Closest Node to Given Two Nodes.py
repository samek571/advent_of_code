class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def bfs(root, cost):
            queue = collections.deque([(root, 0)])
            seen = {root}
            while queue:
                node, step = queue.popleft()
                cost[node] = min(cost[node], step)

                if edges[node] != -1 and edges[node] not in seen:
                    seen.add(edges[node])
                    queue.append((edges[node], step + 1))


        cost1 = [100000]*n ; cost2 = [100000]*n
        bfs(node1, cost1)
        bfs(node2, cost2)

        ans = -1 ; cost = 100000
        for i in range(n):
            if cost > max(cost1[i], cost2[i]):
                cost = max(cost1[i], cost2[i])
                ans = i

        return ans
