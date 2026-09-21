# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # my idea here is to basically loop through the head
        # store the nodes that i've already seen in a set
        # if the current node is somethign that i've seen then i know its a cycle


        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
            

        return False
        