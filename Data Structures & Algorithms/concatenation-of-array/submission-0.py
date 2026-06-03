class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxRange = (n * 2)
        ans = [0] * maxRange

        for i in range(maxRange):
            if i >= n:
                ans[i] = nums[i - n]
            else:
                ans[i] = nums[i]
            

        return ans

        