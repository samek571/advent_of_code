class Solution:
    '''
    its worth editing continous substring from the left even if it is just 1 digit because that position has better value;
    621 to 699 is less than 721 and again we end once it stops being profitable for us, same logic as before
    '''
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        num = list(num); mutated = False

        for idx, n in enumerate(num):
            n = int(n)
            
            if change[n] > n:
                num[idx] = str(change[n])
                mutated = True
            
            elif change[n] < n and mutated: break
        
        return "".join(num)
