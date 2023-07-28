class ZigzagIterator:
    '''to the followup:
    assume we have them in an array then we make one iteration to get each lenght O(k) so far
    then we know we take m[0-k][0] and in this step we check if there will be this array existing in the next iteration
    if yes nothing happens and if not we know we decrease our k by one. Its probably for the best to keep 1-k numbers in a heap of some sort because the shortest array might be not the last one so there will be dificulties handling the elements 
    make a big array of lenght(sum lenghts) and insert accordingly ^^
    '''
    def __init__(self, v1: List[int], v2: List[int]):

        n,m = len(v1), len(v2)
        arr = [] ; i=0

        while min(n,m) > i:
            arr.append(v1[i])
            arr.append(v2[i])
            i+=1
        
        if n<m:
            arr += v2[i:]
        else: arr += v1[i:]

        
        self.arr = collections.deque(arr)


    def next(self) -> int:
        return self.arr.popleft()
        

    def hasNext(self) -> bool:
        return len(self.arr) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
