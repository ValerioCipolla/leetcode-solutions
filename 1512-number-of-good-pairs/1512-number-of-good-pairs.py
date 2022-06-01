class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i, curr in enumerate(nums):
            for next in nums[i + 1:]:
                if curr == next:
                    count += 1
        return count