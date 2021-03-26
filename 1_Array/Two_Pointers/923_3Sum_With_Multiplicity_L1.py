class Solution:
    def threeSumMulti(self, arr: List[int], t: int) -> int:
        cnt = [0] * (100+1)
        for a in arr: cnt[a] += 1
        ans = 0
        for i in range(t+1):
            for j in range(i, t+1):
                k = t - i - j
                if k<0 or k>=len(cnt) or k<j: 
                    continue
                if not cnt[i] or not cnt[j] or not cnt[k]:
                    continue
                if i==j and j==k:
                    ans += (cnt[i]-2)*(cnt[i]-1)*cnt[i]/6
                elif i==j and j!=k:
                    ans += cnt[i] * (cnt[i]-1) / 2 * cnt[k]
                elif i!=j and j==k:
                    ans += cnt[i] * (cnt[j]-1) * cnt[j] / 2
                else:
                    ans += cnt[i] * cnt[j] * cnt[k]
        return int(ans) % (10**9+7)
