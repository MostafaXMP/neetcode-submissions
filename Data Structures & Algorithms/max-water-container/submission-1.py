class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mylist =[]
        # width is the length between 2 indeces
        # hight is the length of the minimum of them
        # volum = width * hight
        # we need to maximize volum
        # then we need to maximize the width and hight
        # I want to make the excess
        # i may need to store the value: [indeces]
        # then get the 
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res