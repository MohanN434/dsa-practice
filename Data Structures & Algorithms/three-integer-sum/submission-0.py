class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i in range(len(nums)):
            target = 0 - nums[i]
            mpp = defaultdict(int)

            for j in range(i + 1, len(nums)):
                rem = target - nums[j]
                if rem in mpp:
                    values = [nums[i], nums[j], nums[mpp[rem]]]
                    values.sort()
                    res.add(tuple(values))

                mpp[nums[j]] = j

        return list(list(x) for x in res)