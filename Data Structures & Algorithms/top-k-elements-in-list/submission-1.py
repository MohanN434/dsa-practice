from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        mpp = defaultdict(int)
        res = []

        for num in nums:
            mpp[num] += 1

        for n, c in mpp.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, - 1):
            for val in freq[i]:
                if len(res) == k:
                    return res
                res.append(val)
        
        return res