"""
Find the upper bound and brute force all the candidates by odd and even cases.
"""


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        L, R = int(L), int(R)
        U, ans = 100000, 0
        for i in range(U):
            s = str(i)
            odd = s + s[:-1][::-1]
            cand = int(odd)**2
            if cand > R:
                break
            if cand >= L and str(cand) == "".join(list(str(cand))[::-1]):
                ans += 1
        for i in range(U):
            s = str(i)
            even = s + s[::-1]
            cand = int(even)**2
            if cand > R:
                break
            if cand >= L and str(cand) == "".join(list(str(cand))[::-1]):
                ans += 1
        return ans
