class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        hashmap = defaultdict(list)
        
        for s in strs:
            sort = ''.join(sorted(s))
            hashmap[sort].append(s)

        ans = []
        for value in hashmap.values():
            ans.append(value)
        return ans