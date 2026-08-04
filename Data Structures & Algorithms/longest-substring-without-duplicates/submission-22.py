class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        char_index = {}
        l = 0

        for r in range(len(s)):
            if s[r] in char_index:
                l = max(l, char_index[s[r]]+1)
            char_index[s[r]] = r
            maximum = max(maximum, r-l+1)
        return maximum

