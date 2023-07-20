# Two-pointer String

# Optimal
# space complexity: O(n + m)
# time complexity: O(n + m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = [""] * (len(word1) + len(word2))
        i, j = 0, 0

        while j < len(word1) and j < len(word2):
            ans[i] = word1[j]
            ans[i + 1] = word2[j]
            i += 2
            j += 1

        while j < len(word1):
            ans[i] = word1[j]
            i += 1
            j += 1

        while j < len(word2):
            ans[i] = word2[j]
            i += 1
            j += 1
        return "".join(ans)
