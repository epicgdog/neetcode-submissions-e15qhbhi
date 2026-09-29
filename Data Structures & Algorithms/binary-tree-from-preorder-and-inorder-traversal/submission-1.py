# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: children first before the root
        # inorder: left root right
        # loop through the preorder then use in order to see where it is located on the tree
        # you already know the preorder starting is the root, go from there.
        # run through the built tree each time
        # loc = dict() # holds location data, or what index each number is at
        # r = None
        # for val in preorder:
        #     new_node = TreeNode(val=val, left=None, right=None)
        #     loc[val] = inorder.index(val)

        #     if not r:
        #         # set teh root
        #         r = new_node
        #         continue

        #     node = r
        #     while node:
        #         curr_idx = loc[node.val]
        #         target_idx = loc[new_node.val]
        #         if target_idx > curr_idx:
        #             if not node.right:
        #                 # easy, just set that ho
        #                 node.right = new_node
        #                 break
        #             else:
        #                 node = node.right
        #         else:
        #             if not node.left:
        #                 node.left = new_node
        #                 break
        #             else:
        #                 node = node.left

        # return r

        # don't have ot mkae on the fly, this would be constant
        loc = {val: i for i, val in enumerate(inorder)}
        it = iter(preorder)

        def build(low, high):
            if low > high:
                return None
            curr_val = next(it)
            curr_node = TreeNode(curr_val)
            curr_node.left = build(low, loc[curr_val] - 1)
            curr_node.right = build(loc[curr_val] + 1, high)
            return curr_node

        return build(0, len(inorder) - 1)
