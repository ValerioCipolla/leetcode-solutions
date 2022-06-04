class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dist_nums = list(set(nums))
        if len(dist_nums) < 3:
            return max(dist_nums)
        dist_nums.sort()
        return dist_nums[-3]