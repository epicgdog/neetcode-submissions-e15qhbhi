# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # easiest way is to loop through every node in the tree and compare to the subroot tree
        # find the first node that equals that value
        # traverse tree and make sure it lines up
        # what if its like all the same number it would be cooked!

        
        def checkTree(a, b): # b is our subtree
            # if b is a leaf, a must also be a leaf
            if a == None and b == None:
                return True
            if a == None or b == None:
                return False
            if a.val != b.val:
                return False
            
            return checkTree(a.left, b.left) and checkTree(a.right, b.right)

        # bfs traversal
        d = deque([root])
        
        while len(d) > 0:
            curr = d.popleft()
            if checkTree(curr, subRoot):
                return True
            if curr.left != None:
                d.append(curr.left)
            if curr.right != None:
                d.append(curr.right)
        return False


        



        