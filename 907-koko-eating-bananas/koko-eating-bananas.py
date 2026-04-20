class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = 0
        while low <= high:
            speed = (low + high) // 2
            count = 0
            for n in piles:
                count += ((n - 1)// speed) + 1
            #print(f'try speed {speed} hours {count}')
            #if count worked, try lower (better) speed
            if count <= h:
                high = speed - 1
                ans = speed
            #didn't work, try higher (worse) speed
            else:
                low = speed + 1
        return ans
