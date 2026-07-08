class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        newSet = {}
        res = [0] * len(nums1)

        for i, n in enumerate(nums2):
            newSet[n] = i

        for i in range(len(nums1)):
            res[i] = newSet[nums1[i]]

        return res