class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accounts = list(map(lambda x: sum(x), accounts))
        return max(accounts)