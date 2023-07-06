# Array Hash-table Stack Monotonic-stack

#  :type nums1: List[int]
#  :type nums2: List[int]
#  :rtype: List[int]

# Brute force
# space complexity: O(n)
# time complexity: O(m * n)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []

        for i in nums1:
            x = -1
            y = None
            for j in range(len(nums2)):
                if nums2[j] == i:
                    y = j
                    break

            for j in range(y, len(nums2)):
                if nums2[j] > nums2[y]:
                    x = j
                    break
            if x > -1:
                res.append(nums2[x])
            else:
                res.append(x)

        return res


# Brute force
# space complexity: O(n)
# time complexity: O(m * n)
class Solution2(object):
    def nextGreaterElement(self, nums1, nums2):
        li = {x: i for i, x in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in li:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = li[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution3(object):
    def nextGreaterElement(self, nums1, nums2):
        li = {x: i for i, x in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = li[val]
                res[idx] = cur
            if cur in li:
                stack.append(cur)

        return res
