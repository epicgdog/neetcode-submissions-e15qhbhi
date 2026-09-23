# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bEquals(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val != q.val:
            return False
        return self.bEquals(p.left, q.left) and self.bEquals(p.right, q.right)
           
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # isn't this just equals another tree but for eveyr node?
        # but that would mean looping through each node mu
        # pretty sure that's the strat

        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        if root.val == subRoot.val and self.bEquals(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        