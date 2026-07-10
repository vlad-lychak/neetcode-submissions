class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charCount = set()

        for r in range(len(s)):
            while s[r] in charCount:
                charCount.remove(s[l])
                l += 1
            charCount.add(s[r])
            res = max(res, len(charCount))
        
        return res
            