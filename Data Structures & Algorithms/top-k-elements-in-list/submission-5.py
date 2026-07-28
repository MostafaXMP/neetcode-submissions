import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) +1

        top_k = [item[0] for item in heapq.nlargest(k, num_freq.items(), key=lambda item: item[1])]
        return top_k
        