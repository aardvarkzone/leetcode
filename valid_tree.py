class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #undirected
        #not cyclical
        #no duplicate edges
        #CANNOT use kahn's for topological sorting -- not directed
        #first check if n - 1 edges
        #then make adjlist, dfs
        #if visited already and not that dfs root, then false
        

        if len(edges) != n - 1: return False

        adjList = defaultdict(list)

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()

        def dfs(vertex, root) -> bool: 
            if vertex in visited and vertex != root:
                return False

            visited.add(vertex)
            for neighbor in adjList[vertex]: 
                if neighbor != root:
                    if not dfs(neighbor, vertex): return False
            return True

        if dfs(0, 0) and len(visited) == n: return True
        else: return False
