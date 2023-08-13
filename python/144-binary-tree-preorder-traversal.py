# Stack Tree Depth-first-search Binary-tree

# Brute force (Recursive)
# space complexity: O(h) (h is the height of the binary tree)
# time complexity: O(n)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res


# Brute force (Iterative)
# space complexity: O(h) (h is the height of the binary tree)
# time complexity: O(n)
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return res


# Optimal (Morris Traversal)
# space complexity: O(1)
# time complexity: O(n)
class Solution3:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        while cur:
            if cur.left == None:
                res.append(cur.val)
                cur = cur.right
            else:
                last = cur.left
                while last.right and last.right != cur:
                    last = last.right

                if last.right == cur:
                    last.right = None
                    cur = cur.right
                else:
                    last.right = cur
                    res.append(cur.val)
                    cur = cur.left
        return res
