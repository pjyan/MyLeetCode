class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if(len(s)<2): return False
        l = s + s
        l = l[1: len(l)-1]
        return s in l
