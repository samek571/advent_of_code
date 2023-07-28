class Solution:
    '''
    changed has to have lenght of 2n and at least n elements divisible by 2
    all - even = odd 
    - if there are some odd numbers they are strictly original --> remove from even their counterparts and each is +1 to counter
    (now is odd empty and even somehow big)
    -else; make one iteration and divide each by 2, each successful location of number in "hashmap/list" is +1 to final counter

    if there is not n pairs its not doubled

    '''


    def findOriginalArray(self, changed: List[int]) -> List[int]:
        length = len(changed)
        if length % 2 != 0:
            return []
        
        freq = [0] * 100001
        for e in changed:
            freq[e] += 1
        
        res = [0] * (length // 2)
        k = 0
        for i in range(100000, 0, -1):
            if freq[i] == 0:
                continue
            if i % 2 != 0 or freq[i] > freq[i//2]:
                return []
            for j in range(freq[i]):
                res[k] = i // 2
                k += 1
                freq[i] -= 1
                freq[i//2] -= 1
                
        return res

#with sort it can be top 90% percentile ...
