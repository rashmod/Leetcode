# Array Prefix-sum
from typing import List

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            res = res * i

        if res > 0:
            return 1
        elif res < 0:
            return -1
        else:
            return 0
