import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        chars = list(clean_text.lower())
        chars_reversed = chars[::-1]
        return chars == chars_reversed
            

        