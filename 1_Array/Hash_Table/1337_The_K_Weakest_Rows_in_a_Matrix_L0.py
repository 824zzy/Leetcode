class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        cnt = Counter()
        for i, r in enumerate(mat): cnt[i] = r.count(1)
        cnt = sorted(cnt.items(), key=lambda x:x[1])
        return [i[0] for i in cnt[:k]]