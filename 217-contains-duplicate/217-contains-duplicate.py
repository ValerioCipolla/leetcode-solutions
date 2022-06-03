import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distincts = list(set(nums))
        if collections.Counter(nums) == collections.Counter(distincts): return False
        else: return True
        