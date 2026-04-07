# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length
        # loop through until n - len, keeping track of prev
        # remove the thing

        sz = 0
        curr = head
        while curr != None:
            sz += 1
            curr = curr.next

        times = sz - n
        curr = head
        prev = None
        for i in range(times):
            prev = curr
            curr = curr.next

        # swap them now
        # if no prev, you are at the start, just remove that ho
        if prev == None: return curr.next
        prev.next = curr.next
        return head

        


        