class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in numbers:
                idx = numbers.index(diff)
                return sorted([i+1, idx+1])
            # if diff == anyother number:
            #     then return index i and the other number's index
        