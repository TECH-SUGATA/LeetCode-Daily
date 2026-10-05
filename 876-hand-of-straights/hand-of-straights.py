from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                times = count[card]

                # Make 'times' groups starting from this card
                for x in range(card, card + groupSize):
                    if count[x] < times:
                        return False
                    count[x] -= times

        return True