""" L2
punchline: i < x % n then we just need to assign extra 1 to current observation.
"""


class Solution:
    def missingRolls(self, A: List[int], mean: int, n: int) -> List[int]:
        x = (len(A) + n) * mean - sum(A)
        if x > 6 * n or n > x:
            return []
        return [x // n + (i < x % n) for i in range(n)]


# brute force simulation


class Solution:
    def missingRolls(self, A: List[int], mean: int, n: int) -> List[int]:
        s = (len(A) + n) * mean
        s_n = s - sum(A)
        if s_n / 6 > n or s_n < 0 or n > s_n:
            return []
        m_n, m_m = divmod(s_n, n)
        if not m_m:
            return [m_n] * n
        else:
            ans = [0] * (n - 1)
            last = m_n + m_m
            cnt = 0
            while last > 6:
                last -= 1
                ans[cnt] += 1
                cnt += 1
            for i in range(len(ans)):
                ans[i] += m_n

            ans = ans + [last]
            return ans
