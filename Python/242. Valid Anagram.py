class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp = [0] * 26
        for i in s:
            tmp[ord(i) - ord('a')] += 1
        for i in t:
            tmp[ord(i) - ord('a')] -= 1
        for i in tmp:
            if i != 0:
                return False
        return True
