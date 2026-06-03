class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}

        for i, num in enumerate(nums):
            rem = target - num

            if rem in exists:
                return [ exists[rem], i ]

            exists[num] = i

        return []
        