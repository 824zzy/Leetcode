""" https://leetcode.com/problems/kth-smallest-instructions/
Given h_cnt and v_cnt to place, we check if it is possible to place H.
If so, decrement h_cnt; otherwise decrement v_cnt and increase the lower bound by number of combinations.
Since there are comb(m+n-1, n-1) instructions starting with H, the condition to check for placing H is comb(m+n-1, n-1)+lower >= k.
"""


class Solution:
    def kthSmallestPath(self, D: List[int], k: int) -> str:
        v_cnt, h_cnt = D[0], D[1]
        ans = ''
        lower = 0
        l = v_cnt + h_cnt
        for i in range(l):
            if h_cnt == 0:
                return ans + (l - i) * 'V'

            num_h = comb(v_cnt + h_cnt - 1, h_cnt - 1)
            if lower + num_h >= k:
                ans += 'H'
                h_cnt -= 1
            else:
                ans += 'V'
                v_cnt -= 1
                lower += num_h
        return ans
