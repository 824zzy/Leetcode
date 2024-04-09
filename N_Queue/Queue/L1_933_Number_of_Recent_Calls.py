""" https://leetcode.com/problems/number-of-recent-calls/
Basic usage of deque: pop old elements from the left
"""


class RecentCounter:
    def __init__(self):
        self.Q = deque()

    def ping(self, t: int) -> int:
        self.Q.append(t)
        while t - 3000 > self.Q[0]:
            self.Q.popleft()
        return len(self.Q)
