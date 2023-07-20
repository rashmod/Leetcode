# Two-pointer String
from typing import List

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        prev = float("inf")
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            prev = nums[i]
            nums[unique] = nums[i]
            unique += 1

        return unique
