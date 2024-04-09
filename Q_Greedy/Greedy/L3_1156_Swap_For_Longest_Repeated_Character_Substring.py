""" https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
learn from lee: https://leetcode.com/problems/swap-for-longest-repeated-character-substring/discuss/355852/Python-Groupby

There are only 2 cases that we need to take care of:
1. extend the group by 1
2. merge 2 adjacent groups together, which are separated by only 1 character
"""


class Solution:
    def maxRepOpt1(self, A: str) -> int:
        cnt = Counter(A)
        A = [(k, len(list(v))) for k, v in groupby(A)]
        # case1: add 1 character to each group
        ans = max([min(v + 1, cnt[k]) for k, v in A])
        # case2: [xxxx][y][xxx]
        for i in range(1, len(A) - 1):
            if A[i][1] == 1 and A[i - 1][0] == A[i + 1][0]:
                ans = max(ans, min(A[i - 1][1] + A[i + 1]
                          [1] + 1, cnt[A[i - 1][0]]))
        return ans
