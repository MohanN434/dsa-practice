class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % len(nums)

        if k == 0:
            return nums

        cutPosition = n - k
        partA = nums[cutPosition:]
        partB = nums[:cutPosition]
        nums[:] = partA + partB