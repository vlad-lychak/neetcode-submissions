class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        res = []
        for i in range(len(arr)):
            arr.pop(0)
            max_in_arr = max(arr, default=-1)
            res.append(max_in_arr)
        return res
        