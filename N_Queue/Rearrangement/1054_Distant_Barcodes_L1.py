class Solution:
    def rearrangeBarcodes(self, A: List[int]) -> List[int]:
        cnt = Counter(A)
        pq = [[-v, k] for k, v in cnt.items()]
        heapify(pq)
        ans = []
        
        while pq:
            tmp = []
            stride = min(len(pq), 2)
            for _ in range(stride):
                v, k = heappop(pq)
                ans.append(k)
                if v+1<0: tmp.append([v+1, k])
            for v, k in tmp: heappush(pq, [v, k])
        return ans