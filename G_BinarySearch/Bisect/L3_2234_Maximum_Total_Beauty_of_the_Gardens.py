""" https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/
refer to: https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/discuss/1931085/Python-Explanation-with-pictures-Greedy.
cost[i] stands for the total cost to make all the gardens before i having the same number of flowers as garden i's.
"""


class Solution:
    def maximumBeauty(
            self,
            A: List[int],
            new: int,
            t: int,
            full: int,
            part: int) -> int:
        A = sorted([min(t, a) for a in A])
        print(A)

        if min(A) == t:
            return full * len(A)
        if new >= t * len(A) - sum(A):
            return max(full * len(A), full * (len(A) - 1) + part * (t - 1))
        # build cost array
        cost = [0]
        for i in range(1, len(A)):
            pre = cost[-1]
            cost.append(pre + i * (A[i] - A[i - 1]))
        print(cost)

        # Since there might be some gardens having `target` flowers already, we
        # will skip them.
        j = len(A) - 1
        while A[j] == t:
            j -= 1

        ans = 0
        while new >= 0:
            # idx stands for the first `j` gardens, notice a edge case might
            # happen.
            idx = min(j, bisect_right(cost, new) - 1)
            # bar is the current minimum flower in the incomplete garden
            bar = A[idx] + (new - cost[idx]) // (idx + 1)
            ans = max(ans, bar * part + full * (len(A) - j - 1))

            # Now we would like to complete garden j, thus deduct the cost for garden j
            # from new and move on to the previous(next) incomplete garden!
            new -= (t - A[j])
            j -= 1
        return ans
