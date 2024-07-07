class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num, i = dict(), 0
        while i <= len(nums) - 1:
            if target - nums[i] in num:
                return [i, num[target-nums[i]]]
            num[nums[i]] = i
            i += 1
        return []
