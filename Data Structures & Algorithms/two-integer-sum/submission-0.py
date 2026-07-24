class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = nums.sort()
        # for i, num in enumerate nums:
        #     num + nums[i+1] = target
        found = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j <= i:
                    continue
                if (nums[i] + nums[j]) == target:
                    found.append(i)
                    found.append(j)
        return found

        