class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index1, index2  = 0, 0
        while index1 < len(haystack):
            if haystack[index1] == needle[index2]:
                if index2 == len(needle) -1:
                    return index1 - index2
                index1 += 1
                index2 += 1
            else:
                index1 = index1 - index2 + 1
                index2 = 0 
        return -1
