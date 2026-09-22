class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        def backtrack(path, total, index):
            if total == target:
                ans.append(path[:])
            if total > target:
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(path, total + candidates[i], i)
                path.pop()
        backtrack([], 0, 0)
        return ans
        