class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            smaller = len(list(filter(lambda x: x < n, nums)))
            res.append(smaller)
        return res