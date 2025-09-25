class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in hashset:
            #if we have no number behind
            #in other words, we are a start
            #of a sequence
            if n - 1 not in hashset:
                streak = n
                streaklen = 1
                #lets check if we have consecutive elements
                while streak + 1 in hashset:
                    streak = streak + 1
                    streaklen = streaklen + 1
                longest = max(longest, streaklen)
        
        return longest
        