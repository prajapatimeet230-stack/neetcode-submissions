class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax =[0]*len(height)
        rightmax = [0]*len(height)
        left = 0
        right = 0
        for i in range(len(height)):            
            left = max(left,height[i])
            leftmax[i] = left

        for j in range(len(height)-1,-1,-1):
            right = max(right,height[j])
            rightmax[j] = right

        total = 0
        for i in range(len(height)):
            water = min(leftmax[i],rightmax[i]) - height[i]
            if water > 0:
                total += water
        return total

            