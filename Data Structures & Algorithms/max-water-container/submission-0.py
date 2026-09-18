class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights)-1

        while i < j:
            area = min(heights[i], heights[j]) * abs(i-j)
            res = max(res, area)

            if heights[i] < heights[j]:
                i += 1
                continue
            
            if heights[i] > heights[j]:
                j -= 1
                continue
            
            if heights[i] == heights[j]:
                i += 1
                continue
        return res
        