class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        #first -- how do we find subarrays with a target sum?
        #can do sliding window 
        #second -- how do we minimize, make sure length is small as possible?
        #brute force or greedy? DPPPP
        if len(arr) == 1:
            return -1
        dp = [math.inf for _ in range(len(arr))]
        left, right = 0, 0
        subarraysum = arr[0]
        ans = math.inf
        bestprev = math.inf
        while left < len(arr) and right < len(arr):
            if subarraysum == target:
                dp[right] = right - left + 1
                bestprev = min(bestprev, dp[right])
                if left > 0:
                    ans = min(ans, dp[left - 1] + dp[right])
                #print(f'target found, {arr[left:right+1]=}, {dp=}, {ans=}')
            else:
                dp[right] = bestprev
            #print(f'{subarraysum=}, {left=}, {right=}')
            if subarraysum >= target:
                subarraysum -= arr[left]
                left += 1
            elif right < len(arr) - 1:
                right += 1
                subarraysum += arr[right]
            else:
                break
        return ans if ans != math.inf else -1
