class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        write = 0
        merged = []

        while write < len(word1) and write < len(word2):
            merged.append(word1[write])
            merged.append(word2[write])
            write += 1

        merged.append(word1[write:])
        merged.append(word2[write:])
        return "".join(merged)