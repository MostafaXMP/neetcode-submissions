class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        value_freq_dict = {}
        for num in nums:
            value_freq_dict[num] = 1+value_freq_dict.get(num,0)

        sorted_keys = sorted(value_freq_dict, key=value_freq_dict.get, reverse=True)
        return sorted_keys[:k]

        