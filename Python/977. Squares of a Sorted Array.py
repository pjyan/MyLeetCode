class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = []
        left, right = 0, len(nums) -1 

        while left <= right:
            if nums[left]**2 >= nums[right]**2:
                l.insert(0,nums[left]**2)
                left = left + 1

            else:
                l.insert(0,nums[right]**2)
                right = right - 1

        return l
