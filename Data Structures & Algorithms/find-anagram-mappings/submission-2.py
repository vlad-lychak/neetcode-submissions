class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        newSet = {}
        res = []

        for i, n in enumerate(nums2):
            newSet[n] = i

        for i, n in enumerate(nums1):
            if n in newSet:
                res.append(newSet[n])

        return res