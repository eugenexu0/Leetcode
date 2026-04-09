class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, start, total = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return -1 if total < 0 else start