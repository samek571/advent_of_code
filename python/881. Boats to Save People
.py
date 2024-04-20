class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        i = 0 ; j = len(people)-1 ; people.sort() ; o=0
        
        while i<=j:
            if people[i]+people[j]<=limit:
                o+=1 ; i+=1 ; j-=1
            else:            
                o+=1 ; j-=1
        
        return o
