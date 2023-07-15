# Array Prefix-sum
from typing import List

# Optimal and naive
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


# Optimal (avoid buffer overflow)
# space complexity: O(1)
# time complexity: O(n)
class Solution2:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for i in nums:
            if i == 0:
                return 0
            neg += 1 if i < 0 else 0

        return -1 if neg % 2 == 1 else 1
