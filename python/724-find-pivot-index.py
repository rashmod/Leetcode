# Array Prefix-sum
from typing import List

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        ans = -1

        for i in range(len(nums)):
            cur = nums[i]
            suffix = (total - cur) / 2
            if prefix == suffix:
                ans = i
                break
            prefix += cur

        return ans
