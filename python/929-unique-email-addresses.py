# Array Hash-table String
from typing import List

# Optimal
# space complexity: O(n)
# time complexity: O(n * m)
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for i in range(len(emails)):
            temp = ""
            plus = False
            for j in range(len(emails[i])):
                if emails[i][j] == "@":
                    temp += emails[i][j:]
                    break

                if plus or emails[i][j] == ".":
                    continue

                if plus or emails[i][j] == "+":
                    plus = True
                    continue

                temp += emails[i][j]
            unique.add(temp)

        return len(unique)


# Optimal with built in functions
# space complexity: O(n)
# time complexity: O(n * m)
class Solution2:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            # email = local + "@" + domain
            # unique.add(email)
            unique.add((local, domain))

        return len(unique)


# Optimal w/o built in functions
# space complexity: O(n)
# time complexity: O(n * m)
class Solution3:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            i, local = 0, ""

            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1

            while e[i] != "@":
                i += 1

            domain = e[i + 1 :]

            # email = local + "@" + domain
            # unique.add(email)
            unique.add((local, domain))

        return len(unique)
