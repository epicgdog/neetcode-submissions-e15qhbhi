# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # ancestor, basically a parent, but can be higher up
        # BST, unique values
        # my thinking is that p and q just define a range right?
        # if you have like 1 9, and your root is 5 you know 5 is the LCA
        # so i'm guessing the way this works is we just traverse the BST and we find (recursively) where the node sort of is in the middle
        # i don't get what to do if hte ancestor is the descendant itself
        # so thats like if the node is equal to p or q, 
        # we can just check if the node falls in the right or left of ts

        min_val = p.val if min(p.val, q.val) == p.val else q.val
        max_val = p.val if max(p.val, q.val) == p.val else q.val
        if (root.val > min_val and root.val < max_val) or root.val == min_val or root.val == max_val:
            # it is in between, or one of the roots is the range, thus we return that root
            return root # this is the common

        # else we move and search
        if root.val < min_val:
            # it is to the right
            return self.lowestCommonAncestor(root.right, p, q)
            
        # it is to the left
        return self.lowestCommonAncestor(root.left, p, q)


        