# Math

# :type x: int
# :rtype: bool

# Brute force
# space complexity: O(n)
# time complexity: O(n)
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        li = [i for i in str(x)]
        print(li)
        start, end = 0, len(li) - 1
        while start <= end:
            if li[start] != li[end]:
                return False
            start += 1
            end -= 1
        return True


# Optimal
# space complexity: O(1)
# time complexity: O(log n)
class Solution2(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev = 0
        orig = x
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
        return rev == orig
