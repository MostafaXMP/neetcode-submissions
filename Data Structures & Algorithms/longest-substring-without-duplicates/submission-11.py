class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        substring = ''
        max_len = 0

        for char in s:
            if char not in substring:
                substring += char
            else:
                l = substring.index(char)
                substring = substring[l+1:]
                substring += char

            max_len = max(max_len, len(substring))
        return max_len

