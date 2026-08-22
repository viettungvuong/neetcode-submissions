from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        # Iterate over unique sorted cards
        for card in sorted(count):
            if count[card] > 0:
                needed = count[card]
                # Consume `needed` amount for all consecutive cards in the group
                for next_card in range(card, card + groupSize):
                    if count[next_card] < needed:
                        return False
                    count[next_card] -= needed

        return True
