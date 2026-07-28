class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_seen_diff = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index_seen_diff:
                return [index_seen_diff[diff], i]
            index_seen_diff[nums[i]] = i
        
