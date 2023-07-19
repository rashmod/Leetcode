# Array Greedy
from typing import List


# Optimal (not mutating the array)
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count, i = 0, 0
        recent = False
        left = 0
        right = flowerbed[i + 1] if length > 1 else 0

        while i + 1 <= length:
            cur = flowerbed[i]
            if cur == 0 and left == 0 and right == 0:
                if recent:
                    recent = False
                else:
                    count += 1
                    recent = True
            else:
                recent = False

            left = cur
            cur = right
            right = flowerbed[i + 2] if i + 2 < length else 0
            i += 1

        return True if count >= n else False


# Optimal (mutating the array)
# space complexity: O(1)
# time complexity: O(n)
class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        left = 0
        right = flowerbed[1] if length > 1 else 0

        for i in range(length):
            if flowerbed[i] == 0 and left == 0 and right == 0:
                flowerbed[i] = 1
                n -= 1

            left = flowerbed[i]
            right = flowerbed[i + 2] if i + 2 < length else 0

        return n <= 0


# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution3:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1
        n -= (empty) // 2

        return n <= 0
