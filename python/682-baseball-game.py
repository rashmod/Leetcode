# Two-pointer String
from typing import List

# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case "C":
                    stack.pop()
                case "D":
                    stack.append(stack[-1] * 2)
                case _:
                    stack.append(int(operations[i]))

        return sum(stack)
