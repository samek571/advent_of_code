class Solution:
    
    ''' anding 2 hashmaps'''
    def getHint(self, secret: str, guess: str) -> str:
        w,f = collections.defaultdict(int), collections.defaultdict(int)
        a,b = 0,0
        for i, num in enumerate(secret):
            if num != guess[i]:
                w[num] += 1
                f[guess[i]] += 1
            else:
                a+=1

        #w and f
        for i in range(11):
            i=str(i)
            if(i in w and i in f):
                b+=min(w[i],f[i])
        return str(a)+"A"+str(b)+"B"
