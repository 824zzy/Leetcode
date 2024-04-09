""" https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
find maximum K elements by heap then use hash table for constructing the subsequence.
"""


class Solution:
    def maxSubsequence(self, A: List[int], k: int) -> List[int]:
        A_neg = list(map(lambda x: x * -1, A))
        heapq.heapify(A_neg)
        freq = Counter()
        while k:
            freq[-1 * heapq.heappop(A_neg)] += 1
            k -= 1

        ans = []
        for x in A:
            if x in freq and freq[x] > 0:
                ans.append(x)
                freq[x] -= 1
        return ans
