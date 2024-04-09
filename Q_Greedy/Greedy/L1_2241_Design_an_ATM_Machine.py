""" https://leetcode.com/problems/design-an-atm-machine/
1. greedily take the amount using available bills as much as possible.
2. if we cannot get the exact amount, then rollback
"""


class ATM:
    def __init__(self):
        self.A = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}
        self.V = [20, 50, 100, 200, 500]

    def deposit(self, cnt: List[int]) -> None:
        for v, c in zip(self.V, cnt):
            self.A[v] += v * c

    def withdraw(self, amt: int) -> List[int]:
        tmp = self.A.copy()
        ans = []
        # check
        for v in reversed(self.V):
            x = min(self.A[v], amt // v * v)
            self.A[v] -= x
            ans.append(x // v)
            amt -= x
        # rollback
        if amt:
            self.A = tmp
            return [-1]
        return ans[::-1]
