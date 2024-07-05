""" https://leetcode.com/problems/k-divisible-elements-subarrays/
Brute force simulation.
note that string join time complexity is O(n)
Time: O(n^3) ~= O(200*200*200) == O(8*10^6)
"""


class Solution:
    def countDistinct(self, A: List[int], k: int, p: int) -> int:
        ans = set()
        A = [str(x) for x in A]
        for i in range(len(A)):
            kk = k
            for j in range(i, len(A)):
                if int(A[j]) % p == 0:
                    kk -= 1
                if kk < 0:
                    break
                ans.add(" ".join(A[i : j + 1]))
        return len(ans)
