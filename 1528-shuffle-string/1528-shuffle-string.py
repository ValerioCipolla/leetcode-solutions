class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s.split()
        arr = list(zip(s, indices))
        arr = sorted(arr, key = lambda x: x[1])
        arr = list(map(lambda x: x[0], arr))
        return "".join(arr)