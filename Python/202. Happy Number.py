class Solution:
    def isHappy(self, n: int) -> bool:
        record = []
        while n not in record:
            record.append(n)
            sum = 0
            strnum = str(n)
            for i in strnum:
                sum += int(i) ** 2
            if sum == 1:
                return True
            else:
                n = sum
        return False
