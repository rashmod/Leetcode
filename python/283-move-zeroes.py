# Array Two-pointers

# :type nums: List[int]
# :rtype: None Do not return anything, modify nums in-place instead.


# Brute force (TLE)
# space complexity: O(1)
# time complexity: O(n^2)
class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] == 0 and j + 1 < len(nums):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


# Brute force (TLE)
# space complexity: O(1)
# time complexity: O(n^2)
class Solution(object):
    def moveZeroes(self, nums):
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
