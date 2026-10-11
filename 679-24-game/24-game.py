from fractions import Fraction

class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        cards = [Fraction(c) for c in cards]
        def testAllOperations(x, y):
            possible = [(x + y), (x - y), (y - x), (x * y)]
            if x != 0:
                possible.append((y / x))
            if y != 0:
                possible.append((x / y))
            return possible
        ans = False
        def backtrack(arr):
            nonlocal ans
            if len(arr) == 1 or ans:
                if arr[0] == 24:
                    ans = True
                return
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    possibleN = testAllOperations(arr[i], arr[j])
                    num1, num2 = arr[i], arr[j]

                    for n in possibleN:
                        copy = arr[:]
                        copy.remove(num1)
                        copy.remove(num2)
                        copy.append(n)
                        backtrack(copy)
        backtrack(cards)
        return ans