class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, weight in times:
            adjList[u].append((weight, v))
        #print(f'{adjList=}')
        heap = [(0, k)]
        dist = [math.inf for _ in range(n + 1)]
        dist[k] = 0
        while heap:
            currdist, node = heapq.heappop(heap)
            if not node in adjList:
                continue
            if currdist > dist[node]:
                continue
            for weight, neighbor in adjList[node]:
                newdist = currdist + weight
                if newdist < dist[neighbor]:
                    dist[neighbor] = newdist
                    heapq.heappush(heap, (currdist + weight, neighbor))
        #print(f'{dist=}')
        ans = max(dist[1:])
        return ans if ans != math.inf else -1