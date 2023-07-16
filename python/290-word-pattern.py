# Hash-table String

# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li = s.split()
        patternHash, sHash = {}, {}

        if len(li) != len(pattern):
            return False

        for i in range(len(li)):
            c1, c2 = pattern[i], li[i]

            if patternHash.get(c1, None):
                if patternHash[c1] != c2:
                    return False
            else:
                patternHash[c1] = c2

            if sHash.get(c2, None):
                if sHash[c2] != c1:
                    return False
            else:
                sHash[c2] = c1

        return True


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li = s.split()
        patternHash, sHash = {}, {}

        if len(li) != len(pattern):
            return False

        for i in range(len(li)):
            c1, c2 = pattern[i], li[i]

            if (c1 in patternHash and patternHash[c1] != c2) or (
                c2 in sHash and sHash[c2] != c1
            ):
                return False

            patternHash[c1] = c2
            sHash[c2] = c1

        return True
