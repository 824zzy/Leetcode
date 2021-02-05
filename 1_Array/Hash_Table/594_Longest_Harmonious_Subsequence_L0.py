class Solution:
    def findLHS(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        ans = 0
        for a in A:
            if a-1 in cnt: ans = max(ans, cnt[a]+cnt[a-1])
            if a+1 in cnt: ans = max(ans, cnt[a]+cnt[a+1])
        return ans