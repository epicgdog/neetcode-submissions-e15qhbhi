# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # better way; just search for both at teh saem time.
        # when they start going separate ways, that's when its over.

        # look for p
        curr = root
        while curr is not None:
            # only move if they are the same
            # cases:
            # if current node is less than p.val and q.val then we can move curr to the right
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right

            # if current node is great than p.val and q.val then we can move curr to the right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            # if they going different ways we know its over.
            elif curr.val > p.val and curr.val < q.val or curr.val < p.val and curr.val > q.val:
                return curr

            # if one of them equals, doesn't that also mean we good?
            elif curr.val == p.val or curr.val == q.val:
                return curr

        return curr
        