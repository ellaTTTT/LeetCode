class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        self.s = [0]*m
        self.tmp = 0
        for i in range(m):
            n = len(accounts[i])
            for j in range(n):
                self.tmp += accounts[i][j]
            self.s[i] = self.tmp
            self.tmp = 0
        return max(self.s)