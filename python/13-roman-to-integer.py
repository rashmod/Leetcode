# Hash-table Math String

# :type s: str
# :rtype: int

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution(object):
    def romanToInt(self, s):
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                res = res - values[s[i]]
            else:
                res = res + values[s[i]]

        return res
