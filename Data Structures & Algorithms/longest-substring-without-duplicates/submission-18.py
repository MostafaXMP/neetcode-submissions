class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        seen = set()
        l = 0

        for char in s:
            while char in seen:
                seen.remove(s[l])
                l+=1
            seen.add(char)
            maximum = max(maximum, len(seen))
        return maximum
