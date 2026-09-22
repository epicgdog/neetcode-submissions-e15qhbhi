# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reorder list
        # i'm pretty sure this is just like you reverse the list
        # then you merge them together, starting with teh actual one
        # if its empty just return
        #actualy not that easy because i didn't read the problem correctly and i was going too fast. 
        # basically you need to use the same nodes as before
        # one half is the ones we keep the same order
        # the other half is the list that we reverse and interleave

        if not head or not head.next:
            return

        slow = head
        fast = head.next
        while fast.next:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
            slow = slow.next

        # slow pointer is the end of hte first half; we can disconnect
        fast_start = slow.next
        slow.next = None

        # reverse the list
        prev = None
        curr = fast_start
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next


        # interleave
        while head:
            head_next = head.next
            head.next = fast
            if fast:
                fast_next = fast.next
                fast.next = head_next
                fast = fast_next
            head = head_next

            
        