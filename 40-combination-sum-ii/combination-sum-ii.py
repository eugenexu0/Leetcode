class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(index, tempTarget, tempCandidates):
            nonlocal ans
            if tempTarget < 0:
                return
            elif tempTarget == 0:
                ans.append(tempCandidates.copy())
                return
            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                tempCandidates.append(candidates[i])
                backtrack(i + 1, tempTarget - candidates[i], tempCandidates)
                tempCandidates.pop()
        backtrack(0, target, [])
        return ans