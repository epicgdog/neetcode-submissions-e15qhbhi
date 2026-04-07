# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs at its core
        # ahve two deques, one for the current nodes, then another to store its children
        # this will be the cycle
        # while there are still children
        # we will keep popping out q then replacing main with children adn building children again.
        if root is None: return []

        main = deque([root])
        children = deque([])
        r = []
    
        while len(main) > 0:

            # loop through each one and place children
            arr = []
            while len(main) > 0:
                node = main.popleft()
                arr.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            r.append(arr)

            # remove the stuff in children and add to the main
            while len(children) > 0:
                main.append(children.popleft())


        return r

        