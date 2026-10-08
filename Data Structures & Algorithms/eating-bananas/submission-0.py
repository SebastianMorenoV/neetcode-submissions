class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return 0

        L = 1
        R = max(piles) 
        
        minEat = 0
        while L <= R:

            k = (L+R) // 2

            ## check how much time k needs to eat...
            time = 0
            for bananas in piles:
                res = bananas / k
                time += math.ceil(res) 
            
            if time <= h:
                minEat = k
                R = k - 1
            elif time > h:
                L = k + 1
        
        return minEat
            
