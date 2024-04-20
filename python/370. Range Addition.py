class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        # the big idea is to mark the starting interval and the ending in a hashmap to make a prefix sum
        # it took me a while to actually comprehend how exactly:
        # maybe it will be no explanation at all but basically we are opening and closing jobs
        # if we get some starting, we mark the interval and it lasts till we say so, therefore it might happen than some arr[i] has multiple jobs and the best time complexity would be to go over the input just once. We can sense the prefix sum from miles away and usually we tend to keep sorted list / matrix whatever, however sort is nlogn so lets use already pre made array to write start/end notation

        arr = [0]*(length+1)

        for s,e,quantity in updates:
            #marking the start
            arr[s]+=quantity

            #marking the end, then we make sure we dont make array longer than "lenght"
            arr[e+1]-=quantity
        arr.pop()


        for i in range(1, length):
            arr[i] += arr[i-1]
        
        return arr
