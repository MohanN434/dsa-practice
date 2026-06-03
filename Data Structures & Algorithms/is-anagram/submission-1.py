class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        baseChar = ord('a')

        for i in range(len(s)):
            count[ ord(s[i]) - baseChar ] += 1
            count[ ord(t[i]) - baseChar ] -= 1

        for i in count:
            if i != 0:
                return False

        return True


        