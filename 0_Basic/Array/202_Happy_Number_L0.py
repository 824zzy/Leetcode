# Google
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while n not in seen:
            seen.append(n)
            n = [int(c)**2 for c in str(n)]
            n = sum(n)
        return True if 1 in seen else False