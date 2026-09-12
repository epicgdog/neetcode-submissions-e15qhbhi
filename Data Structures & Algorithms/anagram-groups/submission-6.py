from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force: compare each string to every other string
        # sort the strings then verify they are equal


        # 100% we have to chck every string to every other one
        # now its just a question of how do we check against each other
        # frequency map or sorting?
        # i'm thinknig frequency map for each one. here's how:


        # loop through all the strings basically and in taht loop generate a frequency map
        # loop through all the other strings and compare to frequency. if not satisfactory then move on
        #  just like hte anagram problem before, check isAnagram. (i feel this uses so much memory tho.)

        hashes = {}
        r = []
        while len(strs) > 0:
            curr_str = strs.pop()
            curr_counter = "".join(sorted(curr_str))

            if curr_counter in hashes:
                hashes[curr_counter].append(curr_str)
            else:
                hashes[curr_counter] = [curr_str]

        for counter_hash in hashes:
            r.append(hashes[counter_hash])
        return r
            
                
            

                


        