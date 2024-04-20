class Solution:
    def smallestRange(self, nums):

        massive = []
        for i , l in enumerate(nums):
            for e in l:
                massive.append((e,i))

        massive.sort(key=lambda x: x[0])

        #sliding window in which there is always at least one element from each array
        hsh={i:None for i in range(len(nums))}
        n = len(nums) ; cnt = 0 ; o = float('inf') ; interval = None

        for ele, i in massive:
            if hsh[i] == None:
                cnt+=1

            hsh[i] = ele


            if cnt==n:
                x = hsh.values()
                a,b = max(x), min(x)
                if o > a-b: interval = [b, a] ; o = a-b


        return interval



def main():
    sol = Solution()
    print(sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])) # return [20,24]
    print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]])) #return [1,1]

if __name__ == "__main__": main()