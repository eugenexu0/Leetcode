class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_freqMap, t_freqMap = {}, {}
        l, r = 0, 0
        resL, resR, minLength = 0, 0, float("inf")
        have = 0
        for i in range(len(t)):
            t_freqMap[t[i]] = t_freqMap.get(t[i], 0) + 1
        need = len(t_freqMap)
        while r < len(s):
            s_freqMap[s[r]] = s_freqMap.get(s[r], 0) + 1
            if s[r] in t_freqMap and s_freqMap[s[r]] == t_freqMap[s[r]]:
                #print(f'adding match {s[r]}')
                have += 1
            #print(s[l:r+1])
            while have == need:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    resL, resR = l, r
                s_freqMap[s[l]] -= 1
                if s[l] in t_freqMap and s_freqMap[s[l]] < t_freqMap[s[l]]:
                    #print("subtracting")
                    have -= 1
                l += 1
            r += 1
        #print(f'l {l}, r {r}')
        #print(minLength)
        return s[resL:resR+1] if minLength != float("inf") else ""
        