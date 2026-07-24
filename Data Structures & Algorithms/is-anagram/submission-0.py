class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # get all the chrachters in s 
        s_list = sorted(list(s))
        # get all the charachters in t
        t_list = sorted(list(t))
        # compare the characters in s and t
        return (s_list == t_list)
        
        