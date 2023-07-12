# Hash-table String Counting

# Brute force
# space complexity: O(n)
# time complexity: O(n * num of balloons)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        li = {}
        for i in text:
            li[i] = li.get(i, 0) + 1

        count = 0

        while True:
            if (
                li.get("b", None)
                and li.get("a", None)
                and li.get("l", None)
                and li.get("o", None)
                and li.get("n", None)
            ):
                if (
                    li["b"] >= 1
                    and li["a"] >= 1
                    and li["l"] >= 2
                    and li["o"] >= 2
                    and li["n"] >= 1
                ):
                    count += 1
                    li["b"] -= 1
                    li["a"] -= 1
                    li["l"] -= 2
                    li["o"] -= 2
                    li["n"] -= 1

                else:
                    break
            else:
                break

        return count


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        li = {}
        for i in text:
            li[i] = li.get(i, 0) + 1

        if (
            li.get("b", None)
            and li.get("a", None)
            and li.get("l", None)
            and li.get("o", None)
            and li.get("n", None)
        ):
            count_b = li["b"]
            count_a = li["a"]
            count_l = li["l"] // 2
            count_o = li["o"] // 2
            count_n = li["n"]

            return min(count_b, count_a, count_l, count_o, count_n)


# Optimal and extendable
# space complexity: O(n)
# time complexity: O(n)
class Solution3:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        balloon, li = {}, {}
        ans = len(text)

        for i in s:
            balloon[i] = balloon.get(i, 0) + 1
        for i in text:
            li[i] = li.get(i, 0) + 1

        for i in balloon:
            ans = min(ans, li.get(i, 0) // balloon[i])
        return ans
