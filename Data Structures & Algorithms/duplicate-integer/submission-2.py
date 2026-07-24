class Solution:
    def num_generator(self, nums):
        for num in nums:
            yield num

    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =set()
        for num in self.num_generator(nums):
            if num in seen:
                return True
            seen.add(num)
        return False
        