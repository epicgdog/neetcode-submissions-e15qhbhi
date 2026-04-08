# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, arr):
        if node is None: 
            return True
        status = self.dfs(node.left, arr)
        if len(arr) >= 1 and arr[-1] >= node.val:
            return False
        arr.append(node.val)
        # len is 0 or arr[-1] < node.val
        return status and self.dfs(node.right, arr)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # validate with an in order traversal
        return self.dfs(root, [])
        
