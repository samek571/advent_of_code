class Solution:
    #stack problem, reverse iteration
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] ; result = []
        for idx in range(len(temperatures)-1, -1, -1):
            temp = temperatures[idx]
            
            #meaning we got closer biggest temp for any further encountered element
            while stack and stack[-1][0] <= temp:
                stack.pop()


            if not stack:
                result.append(0) # obv its the largest
            else:
                result.append(stack[-1][1] - idx) #difference of the greater and current
                
            #regardless, we would like to note the existence so later we can do some poppin'
            stack.append((temp, idx))
        
        return result[::-1]
