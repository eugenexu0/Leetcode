class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = {}
        longestSeen = 0
        tempSeen = 0
        for i, char in enumerate(s):
            if char in hashmap:
                longestSeen = max(longestSeen, tempSeen)
                tempSeen = min(tempSeen, i - hashmap[char] - 1)
            hashmap[char] = i
            tempSeen += 1
        return max(longestSeen, tempSeen)