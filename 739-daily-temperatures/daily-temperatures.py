class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #must be decreasing or equal order, [index, temp]
        for i, t in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][1] < t:
                popped = stack.pop()
                output[popped[0]] = i - popped[0]
            stack.append([i, t])
        return output