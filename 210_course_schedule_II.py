class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #need to return a valid order of courses 
        #use topological sorting to find a DAG
        
        output = []
        adj_list = defaultdict(list)
        for u, v in prerequisites: 
            adj_list[v].append(u)

        num_pre = [0] * numCourses

        for course in adj_list: 
            for neighbor in adj_list[course]: 
                num_pre[neighbor] += 1 

        queue = deque()
        
        for course, prereq_count in enumerate(num_pre):
            if prereq_count == 0: 
                queue.append(course)

        count = 0

        while queue:
            curr = queue.popleft()
            output.append(curr)
            count += 1

            for neighbor in adj_list[curr]:
                num_pre[neighbor] -= 1
                if num_pre[neighbor] == 0: 
                    queue.append(neighbor)
                
            

        if count == numCourses: return output
        else: return []
