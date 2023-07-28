class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # in time marked every change of height, even the non beneficial 
        points = []
        for b in buildings:
            points.append((b[0], -b[2]))
            points.append((b[1], b[2]))
        points.sort() #capping our complexity at nlogn
        

        #algo that basically looks at the relevant points by keeping pq which is sorted layers of height
        ongoingHeight = 0 ; ans = [] ; pq = [0]
        heapq.heapify(pq)
        for i in range(len(points)):
            currentPoint = points[i][0]
            heightAtCurrentPoint = points[i][1]
            
            #each operation is log n
            # obv adding and removing
            if heightAtCurrentPoint < 0:
                heapq.heappush(pq, heightAtCurrentPoint)
            else: #each building has its start and ending so it will be there
                pq.remove(-heightAtCurrentPoint)
                heapq.heapify(pq)
            
            #if there is a change of height because a building rose from the ground
            pqTop = -pq[0]
            if ongoingHeight != pqTop:
                ongoingHeight = pqTop
                ans.append([currentPoint, ongoingHeight])
        
        return ans
