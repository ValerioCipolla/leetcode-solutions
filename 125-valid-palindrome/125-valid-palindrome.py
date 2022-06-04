import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pattern = "[^a-zA-Z0-9]"
        res_str = re.sub(pattern, "", s)
        rev_str = res_str[::-1]
        return rev_str == res_str
        