class Solution:
    """
    topological sorting/kahns review: 
    1) need to check if graph is DAG
    2) first make adj list -- ensure its directed 
    3) create array that holds number of prereqs for that course
    4) create queue that holds all courses without prereqs
    5) while queue, remove current and increment the count of courses
    6) then for every current neighbor, decrement prereq count, and add to queue if 0
    7) now check if the course count is numCourses
    """


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #0 indexed 
        #correct if directed, acyclical (DAG)
        #can use either dfs or topological sorting
        #lets do top sorting
        #first make adj list

        adj_list = defaultdict(list)
        for u, v in prerequisites: 
            adj_list[v].append(u)
        
        #kahns
        #create in-degree array
        #find all nodes with in-degree 0 so no prereqs
        #use queue process these nodes

        #how to count prereqs? check num edges incoming

        prereq_count = [0] * numCourses
    
        for course in adj_list:
            for neighbor in adj_list[course]: 
                prereq_count[neighbor] += 1

        queue = deque()
        
        for course in range(numCourses):
            if prereq_count[course] == 0: queue.append(course)

        #need to process queue
        #decrease count in arr, and then add when count == 0 to queue
        count = 0

        while queue: 
            current = queue.popleft()
            count += 1
            for neighbor in adj_list[current]: 
                prereq_count[neighbor] -= 1
                if prereq_count[neighbor] == 0: 
                    queue.append(neighbor)

        return count == numCourses

        

