class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand = sorted(hand)
        while len(hand) % W == 0 and len(hand) > 0:
            tmp = hand[0]
            for i in range(W):
                try:
                    hand.remove(tmp + i)
                except BaseException:
                    return False
        return True if len(hand) == 0 else False
