class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum, left,right, tmp_len = 0, 0, 0, float("inf")
        while right <= len(nums) - 1:
            sum = sum + nums[right]
            if sum >= target:
                while left <= right and sum - nums[left] >= target:
                    sum = sum - nums[left]
                    left = left + 1
                tmp_len = min(tmp_len, right-left +1)
            right = right + 1

        return tmp_len if tmp_len != float("inf") else 0
