import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mylist = []
        for i, num in enumerate(nums):
            nums[i] = 1
            mylist.append(math.prod(nums))
            nums[i] = num
        # i want to make continue on the specific i of mylist
        
        return mylist
        