class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        nums = [ s := s+x for x in nums]
        return nums