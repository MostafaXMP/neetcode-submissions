class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # begin with the largest width
        # make 2 pointers at the start and end of the heights list
        # multiply the min(start, end) * width
        # save the result in a list
        # move the pointer with the shortest height
        # return the max(result)
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
        return max(results)




