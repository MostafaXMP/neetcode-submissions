class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s, e = 0, len(heights)-1
        results = 0
        while s<e :
            area = min(heights[s] , heights[e]) * (e - s)
            results = max(results, area)
            if heights[s] > heights[e]:
                e -= 1
            else:
                s +=1
        return results




