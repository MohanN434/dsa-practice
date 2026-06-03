class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)

        for n in range(1, len(nums) + 1):
            if n not in numSet:
                return n

        return len(nums) + 1