class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        hashmap = defaultdict(list)
        
        for s in strs:
            sort = ''.join(sorted(s))
            hashmap[sort].append(s)

        return list(hashmap.values())