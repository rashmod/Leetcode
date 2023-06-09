# Array

# :type nums: List[int]
# :rtype: List[int]

# space complexity: O(n)
# time complexity: O(n)
class Solution(object):
    def getConcatenation(self, nums):
        l_nums = len(nums)
        ans = [None] * l_nums * 2
        for i in range(l_nums):
            ans[i] = nums[i]
            ans[i + l_nums] = nums[i]
        return ans


# Extensible
# space complexity: O(n)
# time complexity: O(n)
class Solution2(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(2):
            for j in nums:
                ans.append(j)

        return ans
