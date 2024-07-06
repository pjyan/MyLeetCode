class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low = 0 
        for i in nums:
            if i != val:
                nums[low] = i
                low = low + 1
        return low
