class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #bi-directional
        #unweighted
        #0 - n-1
        #one edge, no self edge

        #approaches DFS

        #1) create adj list with default dict: 
        adj_list = defaultdict(list)
        for u, v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(node) -> bool:
            # Think about:
            # 1. Base case - what if we reach destination? - return true
            if node == destination: return True
            # 2. Mark current node as visited
            visited.add(node)
            # 3. Explore all neighbors for this node
            for next_node in adj_list[node]:
                if next_node not in visited:
                    if dfs(next_node):
                        return True
            # 4. What should we return? - bool
            return False
            
        return dfs(source)
