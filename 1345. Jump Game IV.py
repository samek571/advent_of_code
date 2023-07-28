class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 0
        
        identical = collections.defaultdict(list)
        for i, num in enumerate(arr):
            identical[num].append(i)
        
        q = collections.deque() ; visited = [False] * n
        q.append(0) ; visited[0] = True
        steps = 0
        
        while q:
            size = len(q)
            while size > 0:
                i = q.popleft()
                size -= 1
                if i == n - 1: return steps
                
                next_val = identical[arr[i]]
                next_val.append(i - 1)
                next_val.append(i + 1)
                for next_i in next_val:
                    if 0 <= next_i < n and not visited[next_i]:
                        q.append(next_i)
                        visited[next_i] = True
                next_val.clear()
            steps += 1
        return -1
