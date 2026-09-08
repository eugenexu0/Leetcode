class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #observation:
        #we should pick the most frequently seen task
        #frequency table often changes -> use heap over Counter / map
        
        heap = []
        freqList = Counter(tasks)
        for i, x in freqList.items():
            heap.append([-x, i])
        heapq.heapify(heap)

        queue = deque()

        time = 0
        #print(f'{heap=}')
        while queue or heap:
            time += 1
            #print(f'----------')

            if queue:
                #print(f'{queue[0]=}')
                task, endTime, freq = queue[0]
                if not heap and time < endTime:
                    time = endTime
                if time >= endTime:
                    queue.popleft()
                    heapq.heappush(heap, [freq, task])
            if heap:
                nextTask = heap[0]
                #print(f'{nextTask=}')
                nextTask[0] += 1
                heapq.heappop(heap)
                if nextTask[0] != 0:
                    queue.append((nextTask[1], time + n + 1, nextTask[0]))
            #print(f'{queue=}')
            #print(f'{heap=}')
            #print(f'{time=}')
                
        return time
