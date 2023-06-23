# Array

# :type arr: List[int]
# :rtype: List[int]

# Brute force
# space complexity: O(1)
# time complexity: O(n^2)
class Solution(object):
    def replaceElements(self, arr):
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                continue
            arr[i] = max(arr[i + 1 : len(arr)])

        return arr


# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution2(object):
    def replaceElements(self, arr):
        prev = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = prev
                if temp > prev:
                    prev = temp

        return arr


# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution3(object):
    def replaceElements(self, arr):
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr
