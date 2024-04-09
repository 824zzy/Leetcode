""" https://leetcode.com/problems/longest-subsequence-repeated-k-times/
Observation:
    1. L<8
        Assume the lengthe of repeated subsequence is L, we can obtain: k*L <=n.
        Given n < k*8, ==>  k*L <= n <  k*8
    2. The types of charcter is less than 8 because L<8

1. find all valid candiate characters whose frequency>=k
2. use backtracking to find valid subsequence

Time complexity: O(n*(7^7)) where n is the
"""


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        # valid candidates
        cand = [c for c, v in sorted(freq.items()) if v >= k]

        stk = []
        self.ans = ''

        def dfs():
            # pruning
            if len(stk) > 7:
                return
            for c in cand:
                stk.append(c)
                if check(stk):
                    cur = ''.join(stk)
                    if len(cur) > len(
                        self.ans) or (
                        len(cur) == len(
                            self.ans) and cur > self.ans):
                        self.ans = cur
                    dfs()
                stk.pop()

        def check(A):
            i, cnt = 0, 0
            for c in s:
                if A[i] == c:
                    i += 1
                    if i == len(A):
                        cnt += 1
                        if cnt == k:
                            return True
                        i = 0
            return False

        dfs()
        return self.ans
