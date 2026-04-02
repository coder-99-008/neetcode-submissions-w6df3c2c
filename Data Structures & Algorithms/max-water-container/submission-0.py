class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWaterContent = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            currentWaterContent = min(heights[left], heights[right]) * (right - left)

            maxWaterContent = max(currentWaterContent, maxWaterContent)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        
        return maxWaterContent