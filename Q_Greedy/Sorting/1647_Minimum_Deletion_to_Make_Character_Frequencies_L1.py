""" https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
1. Sort the frequencies in descending order.
2. Find the first index where the frequencies are not existing, and update the counter.
""" 
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        A = sorted(cnt.values(), reverse=True)
        cnt = Counter()
        ans = 0
        
        for x in A:
            while x and x in cnt: 
                x -= 1
                ans += 1
            cnt[x] += 1
        return ans