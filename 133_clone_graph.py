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
        #connected, undirected, unweighted
        #1-indexed, index = value

        if not node: return None #return None instead of [] cause we are returning Node object

        #have a defaultdict to keep track of visited
        visited = defaultdict(Node)
        #key -- original node object
        #value -- copy of node object

        def dfs(node) -> Optional['Node']:
            #if already copied, return copy
            #this means look in visited
            if node in visited: return visited[node]

            #create new copy, process neighbors, return copy
            #make sure to visit
            copy = Node()
            copy.val = node.val
            visited[node] = copy
            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
