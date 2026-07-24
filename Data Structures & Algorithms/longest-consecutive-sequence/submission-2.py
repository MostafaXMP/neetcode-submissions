class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        current_sequence_count = 1
        maximum_sequence = 1
        for i, num in enumerate(nums):
            if i < len(nums)-1:
                if nums[i+1] == num:
                    continue
                if nums[i+1] ==  num + 1:
                    current_sequence_count += 1
                else:
                    current_sequence_count = 1
                maximum_sequence = max(current_sequence_count, maximum_sequence)
        return maximum_sequence
        
