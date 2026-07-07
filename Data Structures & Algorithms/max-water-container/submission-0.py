class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        maxVal = 0

        while r > l:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height

            maxVal = max(maxVal, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxVal
