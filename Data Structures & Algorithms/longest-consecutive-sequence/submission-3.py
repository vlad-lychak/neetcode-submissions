class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        newSet = set(nums)

        for n in newSet:
            if (n - 1) not in newSet:
                count = 1
                while n + count in newSet:
                    count += 1
                res = max(res, count)
        return res