class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1)
        freq1, freq2 = Counter(s1), Counter(s2[left:right])
        while right <= len(s2):
            if freq1 == freq2:
                return True
            freq2[s2[left]] -= 1
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            left += 1
            if right < len(s2):
                freq2[s2[right]] += 1
            right += 1
        return False
            