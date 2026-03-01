class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.a = 0
        def add(x):
            self.a += x
            return self.a
        return list(map(lambda x: add(x), nums))

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.a = 0
        def add(x):
            self.a += x
            return self.a
        return list(map(add, nums))