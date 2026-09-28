class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        L = 0
        R = len(heights) -1

        while L < R:

            minimumH = min(heights[L],heights[R])
            diff = R - L
            area = diff * minimumH
            if area > maxArea:
                maxArea = area

            if heights[L] < heights[R]:
                L+= 1
            else:
                R -=1

        return maxArea