class Solution:
    def bagOfTokensScore(self, T: List[int], P: int) -> int:
        T = sorted(T)
        l, r = 0, len(T)-1
        s = 0
        while l<=r:
            if P>=T[l]:
                s += 1
                P -= T[l]
                l += 1
            elif l<r and s>0:
                P += T[r]
                r -= 1
                s -= 1
            else:
                l += 1
        return s