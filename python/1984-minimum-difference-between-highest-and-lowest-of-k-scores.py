# Array Sliding-window Sorting
from typing import List


# Optimal
# space complexity: O(nlog n + n) (for sorting: nlog n) + (if new array is created: n)
# time complexity: O(nlog n + n) (for sorting: nlog n)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # if the original array should not be mutated
        sNums = sorted(nums, reverse=True)
        # otherwise this
        # nums.sort(reverse=True)
        first, last = 0, 0
        ans = float("inf")
        for i in range(len(sNums) - k + 1):
            first = sNums[i]
            last = sNums[i + k - 1]
            ans = min(ans, first - last)
        return ans
