class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                currentWater = min(heights[i], heights[j]) * (j - i)
                maxWater = max(maxWater, currentWater)

        return maxWater