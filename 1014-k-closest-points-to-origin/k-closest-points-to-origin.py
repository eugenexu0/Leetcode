class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceToOrigin(x, y):
            return math.sqrt(x*x+y*y)
        distances = []
        for x, y in points:
            distances.append((distanceToOrigin(x,y), x, y))
        distances.sort()
        ans = [[x, y] for _, x, y in distances]
        return ans[:k]
        