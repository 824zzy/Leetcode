""" L0: https://leetcode.com/problems/iterator-for-combination/
generate all combinations
"""
# backtracking


class CombinationIterator:
    def __init__(self, S: str, L: int):
        self.S = S
        self.L = L
        self.stk = []
        self.combs = []
        self.dfs(0)

    def next(self) -> str:
        return self.combs.pop(0)

    def hasNext(self) -> bool:
        return len(self.combs) > 0

    def dfs(self, i):
        if len(self.stk) == self.L:
            self.combs.append("".join(self.stk.copy()))
        if i == len(self.S):
            return
        for j in range(i, len(self.S)):
            self.stk.append(self.S[j])
            self.dfs(j + 1)
            self.stk.pop()


# dfs with states


class CombinationIterator:
    def __init__(self, S: str, L: int):
        self.S = S
        self.L = L
        self.combs = []
        self.dfs("", 0)

    def next(self) -> str:
        return self.combs.pop(0)

    def hasNext(self) -> bool:
        return len(self.combs) > 0

    def dfs(self, comb, i):
        if len(comb) == self.L:
            self.combs.append(comb)
        if i == len(self.S):
            return
        for j in range(i, len(self.S)):
            self.dfs(comb + self.S[j], j + 1)
