class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        iterator = iter(nums)

        while True:
            try:
                num = next(iterator)

                if num in seen:
                    return True

                seen.add(num)

            except StopIteration:
                break

        return False