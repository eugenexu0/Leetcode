class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        #bfs kahn's algo
        #calculate in-degree
        adjList = {}
        inDegreeList = {} #node -> inDegree count
        for i in range(numCourses):
            inDegreeList[i] = 0
        for u, v in prerequisites:
            inDegreeList[u] += 1
            if v not in adjList:
                adjList[v] = [u]
            else:
                adjList[v].append(u)
        #put every node with 0 incoming edge in queue
        queue = deque([])
        ans = []
        for node, count in inDegreeList.items():
            if count == 0:
                queue.append(node)
        #decrement each neighbor's in-degree
        #print(f'{adjList=}, {inDegreeList=}, {queue=}')
        while queue:
            #print(f'{node=}')
            node = queue.popleft()
            ans.append(node)
            if node not in adjList:
                continue
            for neighbor in adjList[node]:
                #print(f'neighbor is {neighbor=}, {inDegreeList[neighbor]=}')
                inDegreeList[neighbor] -= 1
                #if neighbor has 0 in-degree, add to queue as well
                if inDegreeList[neighbor] == 0:
                    queue.append(neighbor)
        
        return ans if len(ans) == numCourses else []