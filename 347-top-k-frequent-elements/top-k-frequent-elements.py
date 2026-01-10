class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        #can use Counter but i wont use
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            bucket[value].append(key)
        print(bucket)
        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for j in bucket[i]:
                    ans.append(j)
            if len(ans) == k:
                return ans