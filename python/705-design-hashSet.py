# Array Hash-table Linked-list Design Hash-function

# Naive array solution
# space complexity: O(n)
class MyHashSet:
    def __init__(self):
        self.li = []

    def add(self, key: int) -> None:
        if key >= len(self.li):
            diff = key - len(self.li) + 1
            self.li = self.li + [None] * diff
        self.li[key] = key

    def remove(self, key: int) -> None:
        if key < len(self.li):
            self.li[key] = None

    def contains(self, key: int) -> bool:
        if key < len(self.li) and self.li[key] != None:
            return True
        return False


# Open hashing (separate chaining)
# space complexity: O(n)
class ListNode:
    def __init__(self, key):
        self.val = key
        self.next = None


class MyHashSet2:
    def __init__(self):
        self.set = [ListNode(0) for x in range(10**4)]

    def add(self, key: int) -> None:
        idx = key % len(self.set)
        cur = self.set[idx]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % len(self.set)
        cur = self.set[idx]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        idx = key % len(self.set)
        cur = self.set[idx]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False
