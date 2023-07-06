# Array Two-pointers

# :type nums: List[int]
# :type val: int
# :rtype: int


# Brute force
# space complexity: O(1)
# time complexity: O(n^2)
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            if k > len(nums) - i - 1:
                break
            if nums[i] == val:
                k += 1
                while j > 0 and nums[j] == val and j != i:
                    k += 1
                    j -= 1
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1
        return len(nums) - k


# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution2(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
