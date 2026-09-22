# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # my idea for this is to basically treat the list as a queue
        # we can pop out the last item and hten set that as the starting list
        # then we can run through eveyr other list in the list

        if not lists:
            return



        # my idea was wrong.
        # we have to use the heap method, extract each node and place into a heap
        # this means we can keep popping the heap 
        # this means it is O(nlogk)
        # whereas my solution was O(n*k), which is inefficient when k ~= n
        
        # add just the tips to the heap
        main_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(main_heap, (node.val, i, node))


        # loop through the heap
        # also store whatever comes first
        head_dummy = ListNode()
        result_head = head_dummy
        while main_heap:
            val, i, node = heapq.heappop(main_heap)
            
            # attach to dummy
            result_head.next = node
            result_head = node
            if node.next:
                heapq.heappush(main_heap, (node.next.val, i, node.next))

        return head_dummy.next




        # start_list = lists.pop()
        # while lists:
        #     start_pos = start_list
        #     curr_list = lists.pop()
            
        #     prev = None
        #     while start_pos and curr_list:
        #         if curr_list.val < start_pos.val:
        #             curr_next = curr_list.next
        #             curr_list.next = start_pos
                    
        #             if prev == None:
        #                 # this is the head
        #                 start_list = curr_list
        #             else:
        #                 prev.next = curr_list

        #             prev = curr_list
        #             curr_list = curr_next
        #         else:
        #             prev = start_pos
        #             start_pos = start_pos.next

        #     if prev:
        #         if curr_list:
        #             prev.next = curr_list
        #     else:
        #         if not start_pos and curr_list:
        #             start_list = curr_list
        

        # return start_list



        