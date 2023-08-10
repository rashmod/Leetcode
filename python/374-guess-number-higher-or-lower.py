# Binary-search Interactive

# Optimal
# space complexity: O(1)
# time complexity: O(log n)
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            ans = guess(mid)
            if ans == 0:
                return mid
            if ans == -1:
                high = mid - 1
            if ans == 1:
                low = mid + 1
