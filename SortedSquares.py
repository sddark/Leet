class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for x in range(0,len(nums)):
            nums[x] = nums[x] ** 2
        nums.sort()
        return nums