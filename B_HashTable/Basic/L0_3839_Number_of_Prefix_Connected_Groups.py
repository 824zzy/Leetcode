""" https://leetcode.com/problems/number-of-prefix-connected-groups/
Group words by their first k characters using Counter. Skip words shorter
than k. Count groups with 2+ members.
"""


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        cnt = Counter()
        for w in words:
            if len(w) >= k:
                cnt[w[:k]] += 1
        return sum(1 for _, v in cnt.items() if v > 1)
