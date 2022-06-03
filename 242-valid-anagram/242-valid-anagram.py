class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [c for c in s]
        t = [c for c in t]
        t.sort()
        s.sort()
        return "".join(t) == "".join(s)