class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1

        totalSum = 0
        leftSum = 0
        for i in range(len(nums)):
            totalSum += nums[i]

        for i in range(len(nums)):
            if totalSum - leftSum - nums[i] == leftSum:
                return i
            leftSum += nums[i]
        
        return pivot