""" L3: https://leetcode.com/problems/stone-game-ix/discuss/1500245/JavaC%2B%2BPython-Easy-and-Concise-6-lines-O(n)
TODO:
lee: https://leetcode.com/problems/stone-game-ix/discuss/1500245/JavaC%2B%2BPython-Easy-and-Concise-6-lines-O(n)
ye: https://leetcode.com/problems/stone-game-ix/discuss/1500343/Python3-freq-table
"""
class Solution:
    def stoneGameIX(self, stones):
        cnt = collections.Counter(a % 3 for a in stones)
        if min(cnt[1], cnt[2]) == 0:
            return max(cnt[1], cnt[2]) > 2 and cnt[0] % 2 > 0
        return abs(cnt[1] - cnt[2]) > 2 or cnt[0] % 2 == 0