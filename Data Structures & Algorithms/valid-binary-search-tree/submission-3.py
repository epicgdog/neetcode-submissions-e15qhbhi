# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper function that DFS traversal and is a range so yuo know the max and min of each subtree

        def helper(root, min_range, max_range):
            # we verify the BST basically here
            # verify the root is within the range
            if not root:
                return True
            if root.val >= max_range or root.val <= min_range:
                return False

            return helper(root.left, min_range, root.val) and helper(root.right, root.val, max_range)
            

        return helper(root, -float("inf"), float("inf"))

        