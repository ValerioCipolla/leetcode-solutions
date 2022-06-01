class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        positives = list(filter(lambda x: x >= 0, nums))
        negatives = list(filter(lambda x: x < 0, nums))
        for i in range(len(positives)):
            res.append(positives[i])
            res.append(negatives[i])
        return res
        