class Solution:
    def trap(self, height: List[int]) -> int:
        
        L = 0
        R = len(height) - 1

        maxLeft =  height[L]
        maxRight = height[R]
        water = 0
        while L < R:

            if maxLeft < maxRight:
                L+= 1
                maxLeft = max(maxLeft,height[L])

                water += maxLeft - height[L]
            else:
                R-=1
                maxRight = max(maxRight, height[R])

                water += maxRight - height[R]

        return water
        