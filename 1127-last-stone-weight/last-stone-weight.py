class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-n for n in stones]
        heap = neg_stones
        heapq.heapify(heap)
        print(f'{heap=}')
        while len(heap) > 1:
            stoneA = heapq.heappop(heap)
            stoneB = heapq.heappop(heap)
            if stoneA != stoneB:
                heapq.heappush(heap, -1 * abs(stoneA - stoneB))
        return -1 * heap[0] if len(heap) == 1 else 0
        