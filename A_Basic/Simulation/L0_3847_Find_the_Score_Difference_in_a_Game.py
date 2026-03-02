""" https://leetcode.com/problems/find-the-score-difference-in-a-game/
Simulate the game rules in order: (1) if nums[i] is odd, swap active player,
(2) if every 6th game (index 5, 11, 17, ...), swap active player, (3) active
player scores nums[i]. Track each player as [active_flag, score].
"""


class Solution:
    def scoreDifference(self, A: List[int]) -> int:
        active = 0
        scores = [0, 0]
        for i in range(len(A)):
            if A[i] & 1:
                active ^= 1
            if (i + 1) % 6 == 0:
                active ^= 1
            scores[active] += A[i]
        return scores[0] - scores[1]
