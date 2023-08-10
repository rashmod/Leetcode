# Math Binary-search

# Binary Search Approach
# space complexity: O(1)
# time complexity: O(log n)
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            coins = (mid / 2) * (mid + 1)

            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
                ans = max(ans, mid)
        return ans


# Optimal
# space complexity: O(1)
# time complexity: O(1)
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = 1
        b = 1
        c = -2 * n
        ans = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

        return math.floor(ans)
