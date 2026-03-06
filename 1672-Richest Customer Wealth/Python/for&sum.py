class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        self.s = [0]*m
        for i in range(m):
            n = len(accounts[i])
            self.s[i] = sum(accounts[i])
        return max(self.s)