# String

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        start = False
        length = 0
        while i >= 0:
            if s[i] == " " and start:
                break

            if s[i] != " ":
                start = True

            if start:
                length += 1
            i -= 1
        return length


# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
