""" https://leetcode.com/problems/partition-labels/
1. use a hash table to record the right most index of a character
2. use extra pointer r to indicate the right most of a partition
3. when j reaches the right most index, then update two pointers
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {c: i for i, c in enumerate(s)}
        ans = []
        i = 0
        r = 0
        for j in range(len(s)):
            r = max(r, mp[s[j]])
            if r == j:
                ans.append(j - i + 1)
                i = j + 1
        return ans
