class Solution:

    def encode(self, strs: List[str]) -> str:
        # add a prefix that can be used
        # what should the prefix be if each string can have any character?
        # can' ti pick any thijgn because it will be the first character after?
        # so prefix and then a separate character
        r = []
        for curr_str in strs:
            str_len = len(curr_str)
            r.append(f"{str_len}#{curr_str}")
        return "".join(r)


    def decode(self, s: str) -> List[str]:
        # when decoding, you would use like substring and parse the string out of it based on the index

        r = []
        left_idx = 0
        while left_idx < len(s):
            # process the string
            prefix_idx = s.find("#", left_idx)
            str_len = int(s[left_idx:prefix_idx])
            r.append(s[prefix_idx+1:prefix_idx+1+str_len])
            left_idx = prefix_idx+1+str_len

        return r
            
