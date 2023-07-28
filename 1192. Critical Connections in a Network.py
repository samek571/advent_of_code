class Solution:
    def dfs(self, v, parent):
        self.low[v] = self.timer
        self.disc[v] = self.timer
        self.timer += 1
        self.visited.add(v)

        for to in self.adj[v]:
            if to == parent:
                continue
            elif to in self.visited:
                self.low[v] = min(self.low[v], self.disc[to])
            else:
                self.dfs(to, v)
                self.low[v] = min(self.low[v], self.low[to])

                if self.low[to] > self.disc[v]:
                    self.crit.append([v, to])

    def criticalConnections(self, n: int, connections):
        self.timer = 0
        self.visited = set()
        self.low, self.disc = {}, {}
        self.crit = []
        self.adj = {k: [] for k in range(n)}

        for i, j in connections:
            self.adj[i].append(j)
            self.adj[j].append(i)

        self.dfs(0, -1)

        return self.crit