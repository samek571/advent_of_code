class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
            #return digits[:-1] + [digits[-1]+1]

        else: 
            cnt=0
            while digits and digits[-1]==9:
                cnt+=1
                digits.pop()
            
            if not digits:
                return [1]+[0]*cnt
            else:
                digits[-1]+=1
                return digits + [0]*cnt
