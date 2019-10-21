class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for cs, ct in zip(s, t):
            try:
                if d[cs] != ct:
                    return False
            else:
                if ct in d.values():
                    return False
                d[cs] = ct
        return True