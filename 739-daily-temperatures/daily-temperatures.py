class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #represents indexes, monotonic decreasing/equal stack
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                popped = stack.pop()
                output[popped] = i - popped
            stack.append(i)
        return output