"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs is more aura and way faster
        # i swear i had the right approach earlier but i just gave up on myself
        # standard BFS implementation
        # loop through all of the neighbors
        # if already in the hashmap don't add to queue; else make a new node to add to hashmap
        # add this newly made node to current adjacency list
        if node == None:
            return None

        d = deque([node])
        new_node = Node(node.val)
        hashmap = {node : new_node}
        while len(d) > 0:
            curr = d.popleft()
            for neighbor in curr.neighbors:
                if not neighbor in hashmap:
                    new_neigh = Node(neighbor.val)
                    hashmap[neighbor] = new_neigh
                    d.append(neighbor)
                
                hashmap[curr].neighbors.append(hashmap[neighbor])

        return hashmap[node]
        
        
        # create a hashmap to store the nodes we alr made
        # use DFS to traverse graph one node at a time
        # make a new node for the root, put into hash
        # go through each neighbor and dfs each one
        # if neighbor encounters a cycle, broken since the node will already be in the hashmap so no endless DFS
        # return the starting node

        # def dfs(root):
        #     if root == None:
        #         return

        #     if root in hashmap:
        #         return hashmap[root]

        #     new_node = Node(val=root.val, neighbors=[])
        #     hashmap[root] = new_node

        #     for neighbor in root.neighbors:
        #         new_node.neighbors.append(dfs(neighbor))

        #     return new_node

        # return dfs(node)
        