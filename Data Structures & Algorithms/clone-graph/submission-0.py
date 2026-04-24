"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a hashmap to store the nodes we alr made
        # use DFS to traverse graph one node at a time
        # make a new node for the root, put into hash
        # go through each neighbor and dfs each one
        # if neighbor encounters a cycle, broken since the node will already be in the hashmap so no endless DFS
        # return the starting node

        hashmap = defaultdict(dict)

        def dfs(root):
            if root == None:
                return

            if root in hashmap:
                return hashmap[root]

            new_node = Node(val=root.val, neighbors=[])
            hashmap[root] = new_node

            for neighbor in root.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node)
        