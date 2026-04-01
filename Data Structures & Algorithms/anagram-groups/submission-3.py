from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # setup the dictinoary
        # go through each of the strings
        # frequency analysis, go through each of the strings adn find how frequent everythign is
        # create a key based on that, include all values for every character.
        # if this key already exists, add to the list holding that
        # else, just make a new entry and a new list holding that string
        # loop through this hashmap and add each list ot the return list


        h = defaultdict(list)
        r = []
        a_const = ord("a")
        
        for s in strs:
            freq_arr = [0 for i in range(26)]
            for ch in s:
                # position would be calc as ch - 'a'
                
                pos = ord(ch) - a_const
                freq_arr[pos] += 1
            key = tuple(freq_arr)
            h[key].append(s)
        
        return list(h.values())


        