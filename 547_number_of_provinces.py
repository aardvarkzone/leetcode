class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #undirected
        #need to find number of connected components
        #use DFS, first convert to adjList
        #use set to check for visited
        #then iterate through all vertices,
        #if not visited from DFS, start a new province
        #- you do not need to actually find all the provinces

        adjList = defaultdict(list)
        output = 0
        
        for vertex, neighbors in enumerate(isConnected):
            for neighbor, edge in enumerate(neighbors): 
                if edge: #only need to add one way b/c matrix is symmetric
                    adjList[vertex].append(neighbor)
        
        visited = set()

        def dfs(vertex):
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in adjList[vertex]:
                    #everytime DFS starts from unvisited node, incr output
                    dfs(neighbor)

        #now go through every vertex
        for vertex in range(len(isConnected)):
            if vertex not in visited: 
                output += 1 
                dfs(vertex)

        return output
