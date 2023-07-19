# Two-pointers String Greedy


# Brute Force
# space complexity: O(n)
# time complexity: O(n^2)
class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            new_s = s[:i] + s[i + 1 :]
            if self.is_palindrome(new_s):
                return True
        return False


# Optimal (python cheat)
# space complexity: O(1)
# time complexity: O(n)
class Solution2:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                break

            left += 1
            right -= 1

        i, j = left + 1, right
        while i <= j:
            if s[i] != s[j]:
                break

            i += 1
            j -= 1
        else:
            return True

        i, j = left, right - 1
        while i <= j:
            if s[i] != s[j]:
                break

            i += 1
            j -= 1
        else:
            return True

        return False


# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution3:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        skipLeft, skipRight = True, True

        while left <= right:
            if s[left] != s[right]:
                break

            left += 1
            right -= 1

        i, j = left + 1, right
        while i <= j:
            if s[i] != s[j]:
                skipLeft = False
                break

            i += 1
            j -= 1

        i, j = left, right - 1
        while i <= j:
            if s[i] != s[j]:
                skipRight = False
                break

            i += 1
            j -= 1

        return skipLeft or skipRight


# Optimal (helper methods)
# space complexity: O(1)
# time complexity: O(n)
class Solution4:
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left <= right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        skipLeft, skipRight = True, True

        while left <= right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(
                    s, left, right - 1
                )

            left += 1
            right -= 1

        return True


# Optimal (python cheat)
# space complexity: O(1)
# time complexity: O(n)
class Solution5:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                skipLeft = s[left + 1 : right + 1]
                skipRight = s[left:right]
                return (skipLeft == skipLeft[::-1]) or (skipRight == skipRight[::-1])

            left += 1
            right -= 1

        return True
