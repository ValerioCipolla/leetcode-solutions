class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for n in nums:
            if n == target or n > target:
                return nums.index(n)
        return len(nums)
            
        