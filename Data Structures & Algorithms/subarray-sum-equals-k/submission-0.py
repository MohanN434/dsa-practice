class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = prefix = 0
        sumMap = {0:1}

        for num in nums:
            prefix += num
            rem = prefix - k

            res += sumMap.get(rem, 0)
            sumMap[prefix] = sumMap.get(prefix, 0) + 1

        return res