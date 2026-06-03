class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        largestCount = 0

        for num in nums:
            check = num
            count = 0
            if (check - 1) not in numSet:
                count += 1
                while (check + 1) in numSet:
                    count += 1
                    check += 1
            largestCount = max(largestCount, count)

        return largestCount
            