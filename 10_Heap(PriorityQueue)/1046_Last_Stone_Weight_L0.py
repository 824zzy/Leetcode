class Solution:
    def lastStoneWeight(self, S: List[int]) -> int:
        S = [-s for s in S]
        heapq.heapify(S)
        while len(S)>1:
            x, y = heapq.heappop(S), heapq.heappop(S)
            if x!=y: heapq.heappush(S, x-y)
        return -S[0] if len(S)==1 else 0