class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'}': '{', ']': '[', ')': '('}
        stack = []

        for ch in s:
            if ch in hashMap:
                if not stack or hashMap[ch] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
            
        return len(stack) == 0