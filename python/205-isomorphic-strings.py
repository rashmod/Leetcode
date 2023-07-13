# Hash-table String

# Failed
# int overflowed
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)
        if slen != tlen:
            return False

        x = 1
        for i in range(slen):
            s = s.replace(s[i], str(x))
            t = t.replace(t[i], str(x))
            x += 1

        return True if int(s) == int(t) else False


# Failed
# string size kept increasing and exited loop before traversing the whole string
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)
        if slen != tlen:
            return False

        x = 1
        for i in range(slen):
            s = s.replace(s[i], str(x))
            t = t.replace(t[i], str(x))
            x += 1

        return True if s == t else False


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)
        if slen != tlen:
            return False

        mapST, mapTS = {}, {}
        for i in range(slen):
            c1, c2 = s[i], t[i]
            if mapST.get(c1, None):
                if mapST[c1] != c2:
                    return False
            else:
                mapST[c1] = c2

            if mapTS.get(c2, None):
                if mapTS[c2] != c1:
                    return False
            else:
                mapTS[c2] = c1

        return True


# Optimal
# space complexity: O(n)
# time complexity: O(n)
class Solution4:
    def isIsomorphic(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)
        if slen != tlen:
            return False

        mapST, mapTS = {}, {}
        for i in range(slen):
            c1, c2 = s[i], t[i]
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True
