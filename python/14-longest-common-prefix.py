# String Trie

# :type nums: List[int]
# :type target: int
# :rtype: List[int]

# space complexity: O(m)
# time complexity: O(mn)
# m = len of string
# n = len of array
class Solution(object):
    def longestCommonPrefix(self, strs):
        output = [x for x in strs[0]]
        outputLen = len(output)
        for i in strs:
            if i != strs[0]:
                iLen = len(i)
                while outputLen > 0 and (
                    iLen < outputLen
                    or i[outputLen - 1] != output[-1]
                    or "".join(output) != i[0:outputLen]
                ):
                    output.pop()
                    outputLen = len(output)

        return "".join(output)


# space complexity: O(m)
# time complexity: O(mn)
# m = len of string
# n = len of array
class Solution2(object):
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            res += strs[0][i]
        return res
