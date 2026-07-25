class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s, e = 0, len(heights)-1
        results = 0
        while s<e :
            height = min(heights[s] , heights[e])
            width = e - s
            area = width * height
            results = max(results, area)
            if heights[s] > heights[e]:
                e -= 1
            else:
                s +=1
        return results




