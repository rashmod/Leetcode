# Math Binary-search

# Optimal
# space complexity: O(1)
# time complexity: O(log n)
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        res = 0
        while low <= high:
            mid = low + ((high - low) // 2)  # avoid int overflow
            sq = mid * mid
            if x == sq:
                return mid
            elif x < sq:
                high = mid - 1
            else:
                low = mid + 1
                res = mid
        return res
