# Linked-list Two-pointers

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
