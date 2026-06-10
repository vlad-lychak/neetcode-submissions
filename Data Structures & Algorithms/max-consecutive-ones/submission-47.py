class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        cnt = 0

        for num in nums:
            if num == 0:
                result = max(result, cnt)
                cnt = 0
            else:
                cnt += 1

        return max(result, cnt)