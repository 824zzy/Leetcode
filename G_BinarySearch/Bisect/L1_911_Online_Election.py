""" https://leetcode.com/problems/online-election/
1. use P to find lead person
2. use bisect on T to find correct position
"""


class TopVotedCandidate:
    def __init__(self, P: List[int], T: List[int]):
        self.T = T
        lead = -1
        self.ans = []
        cnt = defaultdict(int)
        for p in P:
            cnt[p] += 1
            if cnt[p] >= cnt[lead]:
                lead = p
            self.ans.append(lead)

    def q(self, t: int) -> int:
        idx = bisect_right(self.T, t)
        return self.ans[idx - 1]
