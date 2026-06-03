from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = defaultdict(int)

        for num in nums:
            mpp[num] += 1

        sortedDict = dict(sorted(mpp.items(), reverse = True, key = lambda item: item[1]))
        keys = list(sortedDict)

        return keys[:k]
        