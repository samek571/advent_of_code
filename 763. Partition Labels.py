class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dick = collections.defaultdict(int)
        for i, e in enumerate(s):
            dick[e]=i
        

        left, right, output = 0, 0, []
        for i, e in enumerate(s):
            right = max(right, dick[e])

            if i == right:
                output.append(-left+right+1)
                left = right+1
        
        return output
