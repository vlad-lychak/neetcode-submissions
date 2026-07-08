class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        largest = -1

        for i in range(len(nums)):
            count[nums[i]] += 1
        
        for key, value in count.items():
            if value == 1 and key > largest:
                largest = key
            
        return largest