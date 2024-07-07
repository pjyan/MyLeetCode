class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        for i in range(0, len(s), 2*k):
            left,right = i, min(len(s)-1, i+k-1)
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        return ''.join(l)
