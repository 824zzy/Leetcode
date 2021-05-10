class Solution:
    def isPossible(self, T: List[int]) -> bool:
        t = sum(T)
        T = [-t for t in T]
        heapq.heapify(T)
        while True:
            ma = -heapq.heappop(T)
            t -= ma
            if ma==1 or t==1: return True
            if ma<t or t==0 or ma%t==0: return False
            ma %= t
            t += ma
            heapq.heappush(T, -ma)
        return len(T)==-sum(T)