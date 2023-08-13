# Stack Tree Depth-first-search Binary-tree

# Brute force (Recursive)
# space complexity: O(h) (h is the height of the binary tree)
# time complexity: O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(head):
            if not head:
                return
            traverse(head.left)
            res.append(head.val)
            traverse(head.right)

        traverse(root)
        return res


# Brute force (Iterative)
# space complexity: O(h) (h is the height of the binary tree)
# time complexity: O(n)
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


# Optimal (Morris Traversal)
# space complexity: O(1)
# time complexity: O(n)
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root

        while cur:
            prev = cur.left
            if prev == None:
                res.append(cur.val)
                cur = cur.right
            else:
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res
