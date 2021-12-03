# use hash table to save id and frequences then return the max frequence.
class Solution:
    def countBalls(self, l: int, h: int) -> int:
        F = collections.Counter()
        for i in range(l, h+1):
            ID = sum([int(c) for c in str(i)])
            F[ID] += 1
        return max(F.values())