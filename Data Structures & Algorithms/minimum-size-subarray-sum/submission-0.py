class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = 0

        l = 0
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLength = ((r - l + 1) if minLength == 0 else min(minLength, r - l + 1))
                currSum -= nums[l]
                l += 1

        return minLength