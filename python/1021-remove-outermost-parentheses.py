# String Stack
from queue import LifoQueue

# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = LifoQueue(maxsize=len(s))
        res = []

        for i in s:
            if i == "(":
                stack.put(i)
                if stack.qsize() > 1:
                    res.append(i)
            if i == ")":
                stack.get()
                if not stack.empty():
                    res.append(i)

        return "".join(res)
