""" L2: Lee215's solution
This time we don't care the count of elements inside the window,
we want to know the count outside the window: we can make the whole string balanced,
as long as max(count[Q],count[W],count[E],count[R]) <= n / 4.
"""
class Solution:
    def balancedString(self, S):
        cnt = Counter(S)
        ans = n = len(S)
        i = 0
        for j, c in enumerate(S):
            cnt[c] -= 1
            while i<n and all(n/4>=cnt[c] for c in 'QWER'):
                ans = min(ans, j-i+1)
                cnt[S[i]] += 1
                i += 1
        return ans