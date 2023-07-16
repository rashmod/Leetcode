# Array Hash-table
from typing import List

# Brute Force (TLE)
# space complexity: O(n)
# time complexity: O(n^2)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(1, len(nums) + 1):
            exists = False
            for j in nums:
                if i == j or i in ans:
                    exists = True
            if not exists:
                ans.append(i)

        return ans


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        s = {}
        ans = []

        for i in range(1, l + 1):
            s[i] = False

        for i in nums:
            s[i] = True

        for i in s:
            if not s[i]:
                ans.append(i)

        return ans


# Optimal (Follow up & in place)
# space complexity: O(1)
# time complexity: O(n)
class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            cur = abs(nums[i])
            nums[cur - 1] = abs(nums[cur - 1]) * -1

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans
