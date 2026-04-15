class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        ans = 1
        prevt = (target - cars[0][0]) / cars[0][1]
        for p, s in cars[1:]:
            t = (target - p) / s
            #if prev car is faster, make new fleet
            if t > prevt:
                ans += 1
                prevt = t
        return ans
