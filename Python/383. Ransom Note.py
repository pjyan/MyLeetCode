class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0]*26
        for i in ransomNote:
            count[ord(i)-ord('a')] += 1
        for i in magazine:
            count[ord(i)-ord('a')] -= 1
        for i in count:
            if i>0:
                return False
        return True
