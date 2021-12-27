""" https://leetcode.com/problems/range-frequency-queries/
create a hash table to find all the indexes for each elements and use bisect to find lower bound and higher bound of indexes.
"""
class RangeFreqQuery:

    def __init__(self, A: List[int]):
        self.loc = defaultdict(list)
        for i, x in enumerate(A):
            self.loc[x].append(i)

    def query(self, l: int, r: int, val: int) -> int:
        idxs = self.loc[val]
        L = bisect_left(idxs, l)
        R = bisect_right(idxs, r)
        return R-L
