class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        freqList = Counter(hand)
        for n in hand:
            canFormHand = True
            for i in range(groupSize):
                if n + i not in freqList or freqList[n + i] == 0:
                    canFormHand = False
                    break
            if canFormHand:
                for i in range(groupSize):
                    freqList[n + i] -= 1

        return False if list(freqList.elements()) else True