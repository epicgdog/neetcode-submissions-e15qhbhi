from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent, 1 means most frequent, 2 means most and second most, etc..
        # generate a frequency map
        #  get max then pop, then get max and pop
        # but how would you pop? not sure
        # also i see in any order, so we can sort these lists then
        # im pretty sure we have to do frequency maps
        # but then again, if i want top k frequent elements, i'm thinking
        # of using a heap here as well. i'd just have to pop stuff off the heap
        # however, i don't remember how to do this, so i will 
        # stick wiht frequency and just basically have an upper limit to check

        nums_freq_map = Counter(nums)
        max_val = -1

        r = []
        for tup in nums_freq_map.most_common(k):
            r.append(tup[0])

        return r



        