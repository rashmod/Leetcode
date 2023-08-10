# Math Binary-search

# Brute force
# space complexity: O(1)
# time complexity: O(sqrt(n))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            sq = i * i
            if num == sq:
                return True
            if num < sq:
                return False


# Optimal
# space complexity: O(1)
# time complexity: O(log n)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = (low + high) // 2
            mid_sq = mid**2
            if num == mid_sq:
                return True
            elif num < mid_sq:
                high = mid - 1
            else:
                low = mid + 1
        return False
