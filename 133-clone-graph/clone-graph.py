"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap = {}
        self.addNode(node, hashmap)
        return hashmap[node]
    
    def addNode(self, node, hashmap):
        if node in hashmap:
            return hashmap[node]
        else:
            hashmap[node] = Node(node.val)
            for neighbor in node.neighbors:
                hashmap[node].neighbors.append(self.addNode(neighbor, hashmap))
        return hashmap[node]