class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        #need to find node with n-1 edges
        #unweighted, non-directional graph
        #make list of number of edges for each node
        #given length of edges is n - 1
        #always valid
        n = len(edges) + 1
        #here we do n + 1 since nodes are from 1 to n
        edgeCount = [0] * (n + 1)
        for a, b in edges:
            edgeCount[a] += 1
            edgeCount[b] += 1
        
        for node, count in enumerate(edgeCount):
            if count == n-1: return node
        
        return 0
