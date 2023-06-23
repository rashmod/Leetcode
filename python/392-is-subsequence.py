# Two-pointers String Dynamic-programming

# :type s: str
# :type t: str
# :rtype: bool

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        return False
