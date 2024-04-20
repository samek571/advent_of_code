class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = collections.defaultdict(list)
        for edge in edges:
            from_node, to_node, cost = edge
            self.graph[from_node].append((to_node, cost))


    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    #dijsktra
    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        visited = set()

        while heap:
            cost, current_node = heapq.heappop(heap)

            if current_node == node2:
                return cost

            if current_node not in visited:
                visited.add(current_node)

                for neighbor, edge_cost in self.graph[current_node]:
                    heapq.heappush(heap, (cost + edge_cost, neighbor))

        return -1
