# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use queues basically and bfs this
        # while stuff in queue
        # we pop 2^i times
        # saves hella space
        # we can't because its not guaranteed its balanced
        # so we have to place in a separate array and then do it again

        if not root:
            return []

        q = deque()
        q.append(root)
        r = []

        while q:
            stuff = []
            new_stuff = []
            while q: 
                node = q.popleft() # empty the queue,
                stuff.append(node.val)
                if node.left:
                    new_stuff.append(node.left)
                if node.right:
                    new_stuff.append(node.right)

            for i in new_stuff:
                q.append(i)

            r.append(stuff)

        return r
            



        