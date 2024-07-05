""" L3 TODO: https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/discuss/1500174/PythonJava-O(N)-greedy-solution-using-a-stack
https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/discuss/1500303/Python3-greedy-via-stack
"""


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, r: int) -> str:
        n_letters = len([c for c in s if c == letter])
        stack = []

        for i, c in enumerate(s):
            while (
                stack
                and stack[-1] > c
                and (len(s) - i + len(stack) > k)
                and (stack[-1] != letter or n_letters > r)
            ):
                d = stack.pop()
                if d == letter:
                    r += 1

            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    r -= 1
                elif k - len(stack) > r:
                    stack.append(c)

            if c == letter:
                n_letters -= 1

        return "".join(stack)
