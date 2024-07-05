""" https://leetcode.com/problems/string-without-aaa-or-bbb/
"""


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ""
        pq = [[-a, "a"], [-b, "b"]]
        heapify(pq)
        while pq:
            if len(pq) == 1:
                ans += -pq[0][0] * pq[0][1]
                return ans
            x, chx = heappop(pq)
            y, chy = heappop(pq)
            # stride can be just 1 or 2
            k = min(-(x - y) + 1, 2)
            for _ in range(k):
                ans += chx
            ans += chy

            if x + k < 0:
                heappush(pq, [x + k, chx])
            if y + 1 < 0:
                heappush(pq, [y + 1, chy])
        return ans
