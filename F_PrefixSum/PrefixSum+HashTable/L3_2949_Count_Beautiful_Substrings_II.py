""" https://leetcode.com/problems/count-beautiful-substrings-ii/
learn from: https://leetcode.cn/problems/count-beautiful-substrings-ii/solutions/2542274/fen-jie-zhi-yin-zi-qian-zhui-he-ha-xi-bi-ceil/

L denotes the length of substring ===> (L/2)^2 % k ==0 ===> L^2 % 4k == 0
    to remove the square of L, we need to find d which d*d % (4*k)==0
"""
from header import *

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        for d in count(1):
            if d*d % (4*k) == 0:
                k = d
                break
                
        cnt = Counter([(k - 1, 0)])  # k-1 和 -1 同余
        ans = pre_sum = 0
        for i, c in enumerate(s):
            pre_sum += 1 if c in "aeiou" else -1
            p = (i % k, pre_sum)
            ans += cnt[p]
            cnt[p] += 1
        return ans