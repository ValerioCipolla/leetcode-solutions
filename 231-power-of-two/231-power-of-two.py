import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        if n < 3: return True
        
        while n > 2:
            n = n / 2
            print(n)
            if n == 2: return True
        return False