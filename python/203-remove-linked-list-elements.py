# Linked-list Recursion

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        new = head
        while new:
            while new.next and new.next.val == val:
                new.next = new.next.next
            new = new.next
        return head


# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
