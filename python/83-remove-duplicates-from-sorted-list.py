# Linked-list

# Optimal
# space complexity: O(1)
# time complexity: O(n)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr, nex = head, head.next
        while nex:
            if curr.val == nex.val:
                curr.next = nex.next
            else:
                curr = curr.next
            nex = nex.next
        return head
