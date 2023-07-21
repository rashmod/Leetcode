# Array Hash-table Sliding-window
from typing import List

# Brute force
# space complexity: O(n)
# time complexity: O(n^2)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        li = {}

        for i in range(len(nums)):
            if li.get(nums[i], None):
                li[nums[i]].append(i)
            else:
                li[nums[i]] = [i]

        ans = float("inf")
        for a in li:
            for b in range(len(li[a])):
                for c in range(b + 1, len(li[a])):
                    ans = min(ans, abs(li[a][b] - li[a][c]))

        return ans <= k


# Optimal
# space complexity: O(k)
# time complexity: O(n)
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
