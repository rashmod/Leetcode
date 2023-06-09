# Hash-table Linked-list Two-pointer

# :type head: ListNode
# :rtype: bool

# Brute force
# space complexity: O(n)
# time complexity: O(n)
class Solution(object):
    def hasCycle(self, head):
        table = {}

        while head:
            if table.get(head, None):
                return True
            table[head] = 1
            head = head.next
        return False


# Floyd's cycle finding algorithm
# tortoise and hare solution
# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution2(object):
    def hasCycle(self, head):
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
