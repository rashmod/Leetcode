# Array Hash-table

# :type nums: List[int]
# :type target: int
# :rtype: List[int]

# Brute force
# space complexity: O(1)
# time complexity: O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution2(object):
    def twoSum(self, nums, target):
        li = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in li:
                return [li[diff], i]
            li[n] = i
