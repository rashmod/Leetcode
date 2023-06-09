# Linked-list Recursion

# :type list1: Optional[ListNode]
# :type list2: Optional[ListNode]
# :rtype: Optional[ListNode]


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# naive solution would be to create new linked list

# in place merge
# space complexity: O(1)
# time complexity: O(n1 + n2)
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = list1 if list1.val <= list2.val else list2

        curr1 = list1 if list1.val <= list2.val else list2
        curr2 = list2 if list1.val <= list2.val else list1
        prev = None

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                prev = curr1
                curr1 = curr1.next
            else:
                temp2 = curr2.next

                prev.next = curr2
                prev = curr2
                curr2.next = curr1
                curr2 = temp2

        if curr1 == None and curr2:
            prev.next = curr2

        return head


# in place merge
# space complexity: O(1)
# time complexity: O(n1 + n2)
class Solution2(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp
        res = list1

        while list1 and list2:
            temp = ListNode()

            while list1 and list1.val <= list2.val:
                temp = list1
                list1 = list1.next

            temp.next = list2
            list1, list2 = list2, list1

        return res
