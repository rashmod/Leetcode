# Array Hash-table
from typing import List

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# with extra memory
# space complexity: O(n)
# time complexity: O(n)
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        stack = []

        for i in s:
            stack.append(i)

        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1


# Recursion
# space complexity: O(n) the space is taken on the call stack
# time complexity: O(n)
class Solution3:
    def reverseString(self, s: List[str]) -> None:
        def reverse(left, right):
            if left <= right:
                s[left], s[right] = s[right], s[left]
                reverse(left + 1, right - 1)

        reverse(0, len(s) - 1)
