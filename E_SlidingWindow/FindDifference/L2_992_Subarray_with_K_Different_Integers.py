""" https://leetcode.com/problems/subarrays-with-k-different-integers/
learn from lee: https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window
if the problem asks the number of subarrays with at most K distinct elements.

exactly(K) = atMost(K) - atMost(K-1),
and use Counter to store seen intergers.
"""


class Solution:
    def subarraysWithKDistinct(self, A: List[int], k: int) -> int:
        def atMost(A, k):
            cnt = Counter()
            i, ans = 0, 0
            for j in range(len(A)):
                cnt[A[j]] += 1
                while len(cnt) > k:
                    cnt[A[i]] -= 1
                    if cnt[A[i]] == 0:
                        del cnt[A[i]]
                    i += 1
                ans += j - i + 1
            return ans
        return atMost(A, k) - atMost(A, k - 1)
