class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_digits = [str(int) for int in digits]
        num = int("".join(string_digits))
        string_result = str(num + 1)
        return string_result      