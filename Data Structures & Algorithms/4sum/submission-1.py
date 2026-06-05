class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                k, l = j + 1, len(nums) - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total < target:
                        k += 1
                    elif total > target:
                        l -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k + 1] == nums[k]:
                            k += 1
                        while k < l and nums[l - 1] == nums[l]:
                            l -= 1
                        k += 1
                        l -= 1

        return res