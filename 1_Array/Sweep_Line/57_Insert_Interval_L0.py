class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        n = max([i[1] for i in intervals])
        dup = []
        cnt = [0] * (n+2)
        for i, j in intervals:
            cnt[i] += 1
            cnt[j] -= 1
            if i==j:
                dup.append(i)
        for i in range(1, n+2):
            cnt[i] += cnt[i-1]
        
        cur = 0
        ans = []
        while cur<len(cnt):
            while cur<len(cnt) and cnt[cur]==0:
                cur += 1
            l = cur
            while cur<len(cnt) and cnt[cur]!=0:
                cur += 1
            if cur<len(cnt) and l<=cur:
                ans.append([l, cur])
        dup2 = dup[:]
        for a in ans:
            for d in dup:
                if a[0]<=d<=a[1]:
                    dup2.remove(d)
        return sorted(ans + [[d, d] for d in list(set(dup2))])