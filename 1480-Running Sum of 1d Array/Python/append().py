class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        res.append(nums[0])
        for i in range(1, n):
            nums[i] = nums[i-1] + nums[i]
            res.append(nums[i])
        return res