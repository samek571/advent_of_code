import collections


class Solution:
    '''make a graph and run bfs'''
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        if source == target: return 0

        #graph
        paths = collections.defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                paths[stop].append(bus)

        if source not in paths or target not in paths: return -1
        
        
        #bfs
        q = collections.deque([source, 0])
        seen = set()
        while q:
            bus_stop, d = q.popleft()
            if bus_stop == target: return d

            if bus_stop not in seen:
                seen.add(bus_stop)

                for next_station in paths[bus_stop]:
                    q.append([next_station, d+1])

        #not connected by any manner of means
        return -1
        
            

def main():
    sol = Solution()
    print(sol.numBusesToDestination([[1,2,7],[3,6,7]], source = 1, target = 6))
    print(sol.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12))
    print(sol.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 13, target = 12))
    print(sol.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 7, target = 13))

if __name__ == "__main__": main()


# class Solution(object):
#     def numBusesToDestination(self, routes, source, target):
#
#
#         buses = defaultdict(list)
#         stops = defaultdict(list)
#
#         for i in range(len(routes)):
#             for j in routes[i]:
#                 buses[j] += [i]
#                 stops[i] += [j]
#
#         queue = [(source, 0)]
#         visited = set()
#
#         while queue:
#
#             stop, num_buses = queue.pop(0)
#
#             if stop == target:
#                 return num_buses
#
#             for bus in buses[stop]:
#                 if bus not in visited:
#                     visited.add(bus)
#                     for nextstop in stops[bus]:
#                         queue.append((nextstop, num_buses + 1))
#
#         return -1



