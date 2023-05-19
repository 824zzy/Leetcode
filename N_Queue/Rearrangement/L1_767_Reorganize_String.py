""" https://leetcode.com/problems/reorganize-string/
767, 1054 are the same

Everytime we select top two frequent characters to fill the string, then update priority queue by new character frequency.
"""
class Solution:
    def reorganizeString(self, s: str) -> str:        
        cnt = Counter(s)
        ans = ''
        pq = [(-v, k) for k, v in cnt.items()] 
        heapify(pq)
        
        while pq:
            stride = min(2, len(pq))
            tmp = []
            for _ in range(stride):
                v, k = heappop(pq)
                ans += k
                if v+1<0: tmp.append([v+1, k])
            if stride==1 and tmp: return ''
            for v, k in tmp: heappush(pq, (v, k))
        return ans