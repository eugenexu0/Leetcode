class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        #idea: detect cycle, if cycle exists, return false
        #perform dfs on each node
        adjList = {}
        for u, v in prerequisites:
            if u not in adjList:
                adjList[u] = [v]
            else:
                adjList[u].append(v)

        visited = set()
        path = set()
        cycleFound = False
        def dfs(node) -> bool:
            nonlocal cycleFound
            #print(f'searching {node=}')
            visited.add(node)
            path.add(node)
            
            if node in adjList:
                for neighbor in adjList[node]:
                    #print(f'{neighbor=}, {path=}, {visited=}')
                    if neighbor in path:
                        #print(f'cycle found')
                        cycleFound = True
                        return
                    if neighbor not in visited:
                        dfs(neighbor)

            path.remove(node)

        #print(f'{adjList=}')
        for node in adjList:
            if node not in visited:
                dfs(node)
        #print(f'{visited=}')
        return (not cycleFound)
            
            
            
        
        

        
