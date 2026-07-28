class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        substring = ""
        for i, char in enumerate(s):
            if char in substring:
                if char != s[i-1] and i != 0:
                    index = substring.index(char)
                    substring = substring[index+1:]
                else:
                    substring = ""
            substring += char
            maximum = max(maximum, len(substring))
            print(substring)
        
        return maximum
