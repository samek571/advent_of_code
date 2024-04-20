class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket= collections.defaultdict(int) ; start= 0

        for fruit in fruits:
            basket[fruit]+= 1

            if len(basket)> 2:
                basket[fruits[start]]-= 1
                
                if basket[fruits[start]]== 0: del basket[fruits[start]]
                start+= 1
        
        
        return len(fruits)- start
