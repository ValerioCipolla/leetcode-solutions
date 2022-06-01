class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum = 0
        for n in nums:
            sum += n
            res.append(sum)
        return res
            