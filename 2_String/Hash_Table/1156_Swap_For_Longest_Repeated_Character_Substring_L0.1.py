from collections import Counter
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        ans = 0
        for i in range(len(text)):
            p = i+1
            n = 1
            curr = text[i]
            while p<len(text) and text[p]==curr:
                n += 1
                p += 1
            p += 1
            while p<len(text) and text[p]==curr:
                n += 1
                p += 1
                
            if cnt[curr]>1:
                ans = max(ans, min(n+1, cnt[curr]))
            else:
                ans = max(ans, min(n, cnt[curr]))
        return ans
    
    
# Lee's solution TODO: figure out what the heck it is
from collections import Counter
class Solution:
    def maxRepOpt1(self, S):
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(S)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in xrange(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res