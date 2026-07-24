class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        encoded = "".join(strs)
        char_count = "❖".join([str(len(string)) for string in strs])
        encoded += "❖" + char_count
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        # 1. Count how many items we expect by counting the separators
        num_words = s.count("❖")
        
        # 2. rsplit("❖", num_words) splits exactly at the metadata boundaries from the right
        parts = s.rsplit("❖", num_words)
        
        # The first element is our complete text block
        strs_blob = parts[0]
        
        # The remaining elements are our multi-digit string lengths
        char_count = [int(x) for x in parts[1:]]
        
        # 3. Slice the text block using our running indices
        mylist = []
        start = 0
        for count in char_count:
            end = start + count
            mylist.append(strs_blob[start:end])
            start = end
            
        return mylist