""" https://leetcode.com/problems/permutation-sequence/
follow db: https://leetcode.com/problems/permutation-sequence/discuss/696390/Python-Math-solution-%2B-Oneliner-both-O(n2)-expained
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        ans, nums = [], list(range(1, n + 1))
        for i in range(n, 0, -1):
            d, k = divmod(k, factorial(i - 1))
            ans.append(nums.pop(d))
        return "".join(map(str, ans))


# simply brute force


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        A = list(permutations(range(1, n + 1)))
        return "".join(list(map(str, A[k - 1])))
