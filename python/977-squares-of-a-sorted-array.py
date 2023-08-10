# Array Two-pointer Sorting
from typing import List

# Brute force
# space complexity: O(nlog n)
# time complexity: O(nlog n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]

        nums.sort()
        return nums


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        left, right = 0, len(nums) - 1
        i = len(nums) - 1

        while left <= right:
            curr = None
            if abs(nums[left]) > abs(nums[right]):
                curr = nums[left]
                left += 1
            else:
                curr = nums[right]
                right -= 1

            res[i] = curr * curr
            i -= 1

        return res
