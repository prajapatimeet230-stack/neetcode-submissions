class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) -1
        res = 0
        while low <  high :
            hei = min(heights[low],heights[high])
            water = hei * (high - low)
            res = max(res , water)
            if heights[low] < heights[high]:
                low += 1
            else :
                high -=1
        return res
        