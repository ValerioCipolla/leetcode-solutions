class Solution:
    def addDigits(self, num: int) -> int:
        digits = [int(n) for n in str(num)]
        num_sum = sum(digits)
        while len(str(num_sum)) > 1:
            digits = [int(n) for n in str(num_sum)]
            num_sum = sum(digits)
        return num_sum
        