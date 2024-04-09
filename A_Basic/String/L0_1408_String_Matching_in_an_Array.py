""" https://leetcode.com/problems/string-matching-in-an-array/
brute force find substrings
"""


class Solution:
    def stringMatching(self, A: List[str]) -> List[str]:
        A.sort(key=len, reverse=True)
        ans = set()
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[j] in A[i]:
                    ans.add(A[j])
        return ans
