import collections 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        counter = 0
        for c in s:
            if c in s_dict: continue
            else: s_dict[c] = counter
            counter += 1
        counter = 0
        for c in t:
            if c in t_dict: continue
            else: t_dict[c] = counter
            counter += 1
        s_counter = []
        t_counter = []
        for c in s:
            s_counter.append(s_dict[c])
        for c in t:
            t_counter.append(t_dict[c])
        if len(s_counter) != len(t_counter): return False
        for i in range(len(s_counter)):
            if s_counter[i] != t_counter[i]: return False
        return True
            