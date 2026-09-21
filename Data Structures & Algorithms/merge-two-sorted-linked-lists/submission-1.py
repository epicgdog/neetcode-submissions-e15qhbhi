# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # loop through both lists at the same time
        # compare pointers
        #  if <= move to the return pointer list
        # else move the other one
        # if there are any else remainng just add them
        # but yeah we'd only loop through as long as both 
        # have something, so if one runs out, we stop the comparisons
        # and we just add whatever was left

        # result should just carry the head node

        if not list1 and not list2:
            return

        result = None
        curr = result
        while list1 and list2:
            if list1.val < list2.val:
                if not result:
                    result = list1
                else:
                    curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                if not result:
                    result = list2
                else:
                    curr.next = list2
                curr = list2
                list2 = list2.next

        if list1:
            if not result:
                return list1
            curr.next = list1
        elif list2:
            if not result:
                return list2
            curr.next = list2
        
        return result

        