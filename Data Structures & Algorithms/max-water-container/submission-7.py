class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s, e = 0, len(heights)-1
        results = []
        while s<e :
            height = min(heights[s] , heights[e])
            width = e - s
            area = width * height
            results.append(area)
            if heights[s] > heights[e]:
                e -= 1
            else:
                s +=1
            res = max(results)
        del results
        return res




