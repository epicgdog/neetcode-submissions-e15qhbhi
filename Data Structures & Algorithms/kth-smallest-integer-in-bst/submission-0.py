# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:


    def dfs(self, root, arr):
        if root is None:
            return

        result = self.dfs(root.left, arr)
        if result:
            return result
        arr.append(root.val)
        self.times -= 1
        if self.times == 1:
            return root.val
        result = self.dfs(root.right, arr)
        if result:
            return result
        
        


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do a total of k iterations
        # stop early in dfs, so keep a parameter that will keep track of which one we are on
        self.times = k + 1
        return self.dfs(root, [])

        