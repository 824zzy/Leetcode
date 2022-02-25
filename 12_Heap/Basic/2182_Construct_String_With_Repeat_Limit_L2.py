""" https://leetcode.com/problems/construct-string-with-repeat-limit/
"""
class Solution:
    def repeatLimitedString(self, s: str, rL: int) -> str:
        pq = [(-ord(k), v) for k, v in Counter(s).items()]
        heapify(pq)
        
        ans = []
        while pq:
            k, v = heapq.heappop(pq)
            if ans and k==ans[-1]:
                if not pq: break
                kk, vv = heappop(pq)
                ans.append(kk)
                if vv-1: heappush(pq, (kk, vv-1))
                heappush(pq, (k, v))
            else:
                m = min(rL, v)
                ans.extend([k]*m)
                if v-m: heappush(pq, (k, v-m))
        return "".join(chr(-x) for x in ans)