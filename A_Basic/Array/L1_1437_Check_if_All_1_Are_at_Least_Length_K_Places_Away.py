# set initial distance by k
class Solution:
    def kLengthApart(self, A: List[int], k: int) -> bool:
        d = k
        for a in A:
            if a == 0:
                d += 1
            elif d >= k:
                d = 0
            else:
                return False
        return True
