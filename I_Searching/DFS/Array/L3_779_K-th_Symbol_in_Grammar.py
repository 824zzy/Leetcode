""" https://leetcode.com/problems/k-th-symbol-in-grammar/
observation: k-th symbol is the flipped in previous row, i.e., k-2**i
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(i, k):
            if k == 1:
                return 0
            if k > 2 ** i:
                return 1 ^ dfs(i, k - 2 ** i)
            else:
                return dfs(i - 1, k)

        return dfs(n, k)
