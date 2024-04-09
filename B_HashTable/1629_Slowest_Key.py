""" L0
Use hash table to simulate
"""


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = defaultdict(int)
        releaseTimes = [0] + releaseTimes
        for i in range(len(keysPressed)):
            duration[keysPressed[i]] = max(
                releaseTimes[i + 1] - releaseTimes[i], duration[keysPressed[i]])
        mi = max(duration.values())
        cand = []
        for k, v in duration.items():
            if v == mi:
                cand.append(k)
        return max(cand)
