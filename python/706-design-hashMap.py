# Array Hash-table Linked-list Design Hash-function

# Open hashing (separate chaining)
# space complexity: O(n)
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 10**4
        self.hashMap = [ListNode(None, None) for x in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        cur = self.hashMap[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        cur = self.hashMap[idx]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        cur = self.hashMap[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
