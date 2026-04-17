class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #key insight:
        #need to find smallest neighbor to left + right
        #to calc width, so monotonic stack is needed
        stack = [] #INDICES
        ans = -1
        for i, n in enumerate(heights):
            while stack and n < heights[stack[-1]]:
                height = heights[stack.pop()]
                #print(f'f {height} * {tempwidth}')
                prev = stack[-1] if stack else -1
                ans = max(ans, height * (i - prev - 1))
            stack.append(i)
        #process remaining stack
        prev = -1
        #print(stack)
        for n in stack:
            #print(f'{heights[n]} and {(len(heights) - prev - 1)}')
            ans = max(ans, heights[n] * (len(heights) - prev - 1))
            prev = n
        return ans
        