# Hash-table Linked-list Two-pointer

# Brute force
# space complexity: O(n + m)
# time complexity: O(n + m)
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        hsh = {}
        head = headA
        while head:
            hsh[head] = True
            head = head.next
        head = headB
        while head:
            if hsh.get(head, None):
                return head
            head = head.next
        return None


# Optimal
# space complexity: O(1)
# time complexity: O(n + m)
class Solution2:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        tempA, tempB = headA, headB
        while tempA != tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA
        return tempA
