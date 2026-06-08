class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        for i in range(len(heights)):
            currentWater = 0
            for j in range(i+1, len(heights)):
                currentWater = max(currentWater, min(heights[i], heights[j]) * (j - i))
            maxWater = max(maxWater, currentWater)

        return maxWater