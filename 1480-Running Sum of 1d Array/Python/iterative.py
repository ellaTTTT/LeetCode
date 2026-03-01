class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums = accumulate(nums)
        return list(nums)