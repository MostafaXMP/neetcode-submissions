class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = []
        mylist = []
        for i in range(len(strs)):
            sorted_strings.append("".join(sorted(strs[i])))

        set_strings = set(sorted_strings)
        for string in set_strings:
            sublist = [strs[index] for index, value in enumerate(sorted_strings) if value == string]
            mylist.append(sublist)
        
        return mylist
        
        