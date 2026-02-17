class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(res: List[int], path: List[int], remain: int, index: int):
            #check if remaining reached 0
            if remain == 0:
                res.append(path.copy())
                return
            #prune if gets below 0
            elif remain < 0:
                return
            #note that index is needed to prevent duplicate paths
            for i in range(index, len(candidates)):
                newpath = path.copy()
                newpath.append(candidates[i])
                backtrack(res, newpath, remain - candidates[i], i)
        res, path = [], []
        backtrack(res, path, target, 0)
        return res