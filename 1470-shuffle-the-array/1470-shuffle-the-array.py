class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        first_arr = nums[:n]
        second_arr = nums[n:]
        for i in range(len(first_arr)):
            res.append(first_arr[i])
            res.append(second_arr[i])
        return res
        