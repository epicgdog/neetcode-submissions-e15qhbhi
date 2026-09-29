# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # immediately i think you have to walk the entire tree
        # and find every single path
        # but how? dfs?

        curr_max = float("-inf")

        def dfs(node):
            nonlocal curr_max
            if not node:
                return 0
            
            curr_max = max(curr_max, node.val)
            if not node.left and not node.right:
                # leaf node, return its value
                return node.val

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            node_right = node.val + right_sum
            curr_max = max(curr_max, node_right)
            
            node_left = node.val + left_sum
            curr_max = max(curr_max, node_left)
            
            total = left_sum + right_sum + node.val
            curr_max = max(curr_max, total)

            return max(node_right, node_left, node.val)

        dfs(root)

        return curr_max



        