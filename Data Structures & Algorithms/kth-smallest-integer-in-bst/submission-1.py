# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # place all the nodes in a queue in order
        # pop k-1 times
        # return the last pop

        q = deque()
        # do an inorder traversal
        def helper(root):
            if not root:
                return
            helper(root.left)
            q.append(root)
            helper(root.right)
        helper(root)

        for i in range(k-1):
            q.popleft()

        return q.popleft().val

        