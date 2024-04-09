""" https://leetcode.com/problems/sender-with-largest-word-count/
sort the hash table on both word count and lexicographic.
"""


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        cnt = Counter()
        for m, s in zip(messages, senders):
            cnt[s] += len(m.split())
        return sorted(
            cnt.items(),
            key=lambda x: (
                x[1],
                x[0]),
            reverse=True)[0][0]
