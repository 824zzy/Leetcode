""" https://leetcode.com/problems/cracking-the-safe/
modified iterative version of:
https://leetcode.com/problems/cracking-the-safe/discuss/1612932/Fast-Python-Hierholzer's
"""


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join(map(str, range(k)))

        P = list(product(range(k), repeat=n))
        nodes = [''.join(map(str, p)) for p in P]

        G = defaultdict(list)
        for node in nodes:
            G[node[:-1]].append(node[1:])

        ans = []
        stk = ['0' * (n - 1)]
        while stk:
            while G[stk[-1]]:
                stk.append(G[stk[-1]].pop())
            ans.append(stk.pop())
        ans.reverse()
        return ''.join([ans[i][0] for i in range(len(ans) - 1)] + [ans[-1]])
