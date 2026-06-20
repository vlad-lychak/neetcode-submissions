class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1

        # while r < len(numbers):
        #     if numbers[l] + numbers[r] == target:
        #         return [l+1, r+1]
        #     else:
        #         r += 1
        
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]