class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        for i, n in enumerate(nums):
            ind[n] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in ind and ind[diff] != i:
                return [i, ind[diff]]