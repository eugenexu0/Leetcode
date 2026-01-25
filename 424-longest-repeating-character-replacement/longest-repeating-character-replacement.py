class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left, ans, maxOccurence = 0, 0, 0
        for i, c in enumerate(s):
            hashmap[c] = 1 + hashmap.get(c, 0)
            maxOccurence = max(maxOccurence, hashmap[c])
            #i - l - 1 is windowsize
            #maxoccurence is the "majority" element
            if (i - left + 1) - maxOccurence > k:
                hashmap[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans