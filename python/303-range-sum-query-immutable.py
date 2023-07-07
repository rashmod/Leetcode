# Array Design Prefix-sum

# :type nums: List[int]

# :type left: int
# :type right: int
# :rtype: int

# Brute force
# space complexity: O(n)
# time complexity: O(n * num of times sumRange is called)
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):

        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class NumArray2(object):
    def __init__(self, nums):
        self.prefix = [None] * len(nums)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.prefix[i] = sum

    def sumRange(self, left, right):
        if left > 0:
            return self.prefix[right] - self.prefix[left - 1]
        return self.prefix[right]
