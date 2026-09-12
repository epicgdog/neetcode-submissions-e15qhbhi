class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # not O(n): just sort and just check the difference


        # its bounded by the maxmimum value right?
        # you can only have at most the maximum value
        # finding max is O(n), so you start wiht that
        # then create a set from the list and ifnd if the next value is there, if not
        # set the max and stuff
        # pretty sure we don't need a frequency ma
        # i don't think that was the right idea
        # i started with 0 but there can be netgatives
        # id have to start wiht the min and then loop tot he max, which can be a huge range. 


        # i think i have to loop through the actual nums thing
        # and then update the previous or something
        # i'm pretty sure you have to start with the minimum value

        # ok i knew you had to have something in a set
        # basically, you need to have the set of numbers in nums (since dupes don't matter)
        # what i was missing was how you start
        # i was right that you had to start form the min
        # but you only really can start from the min
        # so for each num in nums, find if the previous
        # value is in the set,
        # if it isn' t, then yuo know its a minimum and 
        # you can traverse. 

        num_set = set(nums)
        max_count = 0

        for num in nums:
            if num-1 not in num_set:
                # a minimum, we can build up from
                curr_num = num + 1
                count = 1
                while curr_num in num_set:
                    curr_num += 1
                    count += 1

                if count > max_count:
                    max_count = count

        return max_count

                
