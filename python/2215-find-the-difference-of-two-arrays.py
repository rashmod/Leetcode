# Array Hash-table
from typing import List


# Brute Force (TLE)
# space complexity: O(n * m)
# time complexity: O(n * m)
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        li = [[], []]

        for i in nums1:
            exists = False
            for j in nums2:
                if i == j or i in li[0] or j in li[0]:
                    exists = True

            if not exists:
                li[0].append(i)

        for i in nums2:
            exists = False
            for j in nums1:
                if i == j or i in li[1] or j in li[1]:
                    exists = True

            if not exists:
                li[1].append(i)

        return li


# Optimal
# space complexity: O(n + m)
# time complexity: O(n + m)
class Solution2:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        li = [[], []]

        table1, table2 = set(), set()

        for i in nums1:
            table1.add(i)

        for i in nums2:
            table2.add(i)

        for i in table1:
            if i not in table2:
                li[0].append(i)

        for i in table2:
            if i not in table1:
                li[1].append(i)

        return li
