class Solution:
    def numberOfSteps(self, num: int) -> int:
        return len(f"{num:b}")-1 + int(f"{num:b}".count('1'))      