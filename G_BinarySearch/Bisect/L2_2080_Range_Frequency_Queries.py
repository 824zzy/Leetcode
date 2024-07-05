""" https://leetcode.com/problems/range-frequency-queries/
binary serach + hash table
"""


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.cnt = defaultdict(list)
        for i, a in enumerate(arr):
            self.cnt[a].append(i)

    def query(self, l: int, r: int, val: int) -> int:
        i = bisect_right(self.cnt[val], l - 1)
        j = bisect_right(self.cnt[val], r)
        return j - i
