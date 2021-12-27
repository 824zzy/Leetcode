class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        cnt = collections.Counter(s)
        freq = list(cnt.values())
        for i, (k, v) in enumerate(cnt.items()):
            while v in freq[i+1:] and v>0:
                v -= 1
                ans += 1
            freq.append(v)
        return ans