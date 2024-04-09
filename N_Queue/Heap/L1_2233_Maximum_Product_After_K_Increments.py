""" https://leetcode.com/problems/maximum-product-after-k-increments/
lesson learned from contest: DONT THINK TOO MUCH ABOUT TIME COMLEXITY, ALWAYS TRY THE BRUTE FORCE SOLUTION FIRST

Time complexity: O(klogn)
"""


class Solution:
    def maximumProduct(self, A: List[int], k: int) -> int:
        heapify(A)
        while k:
            heappush(A, heappop(A) + 1)
            k -= 1

        ans = 1
        for x in A:
            ans *= x
            ans %= 10**9 + 7
        return ans
