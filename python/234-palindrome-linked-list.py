# Two-pointer String

# Brute force
# space complexity: O(n)
# time complexity: O(n)
from queue import LifoQueue


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = LifoQueue()
        temp = head
        while temp is not None:
            stack.put(temp.val)
            temp = temp.next

        temp = head
        while temp is not None:
            cur = stack.get()
            if cur != temp.val:
                return False
            temp = temp.next
        return True


# Brute force
# space complexity: O(n)
# time complexity: O(n)
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        mid = slow.next
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp

        slow.next = prev
        slow = slow.next

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
