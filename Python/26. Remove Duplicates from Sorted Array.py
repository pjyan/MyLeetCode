class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low,tmp = 0,float("inf")
        for i in nums:
            if i != tmp:
                tmp = i
                nums[low] = i
                low = low + 1
        
        return low
