class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        
        unique_chars = set(s)

        for char in unique_chars:
            for i in range(len(s)):
                currMax, remaining = 0, k

                for j in range(i, len(s)):
                    if char == s[j]:
                        currMax += 1
                    elif remaining > 0:
                        remaining -= 1
                        currMax += 1
                    else:
                        break

                res = max(currMax, res)

        return res