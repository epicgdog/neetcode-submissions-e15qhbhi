# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we need to basically traverse the tree as far down as possible
        # and then count how far it is
        # i'm guessing our stop is when the root is null and we return like 0 or something
        # or we could just calculate the max depth at each level and add thsoe together

        if not root:
            return 0

        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)

        if left_max > right_max:
            return left_max + 1
        
        return right_max + 1


        