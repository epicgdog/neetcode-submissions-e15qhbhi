# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # immediately reverse the list
        # the reversed list has to be new objects tho
        # go through n times adn remove
        # this won't work, we still need the original head
        # just loop through and get the total length
        # then do len - n - 1 to get amount of times to loop through
    
        list_len = 0
        curr = head
        while curr:
            curr = curr.next
            list_len += 1

        loop_times = list_len - n

        edit_list = head
        prev = None
        next_node = head.next
        for i in range(loop_times):
            prev = edit_list
            edit_list = next_node
            next_node = edit_list.next
        
        if not prev:
            # we are removing the head
            return head.next

        prev.next = next_node
        return head





        

        