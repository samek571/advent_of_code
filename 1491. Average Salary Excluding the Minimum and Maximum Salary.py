class Solution:
    def average(self, salary: List[int]) -> float:
        ma, mi = 0, float('inf')

        summ=0
        for i in salary:
            summ+=i
            ma = max(ma, i)
            mi = min(mi, i)
        
        return (summ-mi-ma)/(len(salary)-2)
