class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnts = [collections.Counter(a) for a in A]
        ans = []
        for k, v in cnts[0].items():
            a = 0
            c = v
            for cnt in cnts[1:]:
                if k not in cnt: break
                a += 1
                c = min(c, cnt[k])
            if a==len(cnts)-1: ans += k*c
        return ans