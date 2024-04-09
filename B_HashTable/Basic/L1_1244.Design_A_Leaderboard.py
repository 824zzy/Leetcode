# Contest 12
from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.lb = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.lb[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.lb.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        self.lb.pop(playerId)
        return None
