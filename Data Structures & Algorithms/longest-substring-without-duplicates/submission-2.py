class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, left = 0, 0
        lastSeen = defaultdict(int)

        for right in range(len(s)):
            if s[right] in lastSeen:
                left = max(left, lastSeen[s[right]] + 1)
            lastSeen[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest            
